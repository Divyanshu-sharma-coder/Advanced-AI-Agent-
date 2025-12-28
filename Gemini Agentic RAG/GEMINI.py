import os
import hashlib
import tempfile
from datetime import datetime
from typing import List, Tuple

import streamlit as st
import bs4
import google.generativeai as genai

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_core.embeddings import Embeddings

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "gemini-agentic-rag-prod"
EMBEDDING_DIM = 768

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
EXA_API_KEY = os.getenv("EXA_API_KEY")

assert GOOGLE_API_KEY, "GOOGLE_API_KEY missing"
assert QDRANT_API_KEY, "QDRANT_API_KEY missing"
assert QDRANT_URL, "QDRANT_URL missing"

genai.configure(api_key=GOOGLE_API_KEY)

class GeminiEmbedder(Embeddings):
    def __init__(self):
        self.model = "models/text-embedding-004"

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [
            genai.embed_content(
                model=self.model,
                content=t,
                task_type="retrieval_document"
            )["embedding"]
            for t in texts
        ]

    def embed_query(self, text: str) -> List[float]:
        return genai.embed_content(
            model=self.model,
            content=text,
            task_type="retrieval_query"
        )["embedding"]



def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def init_qdrant() -> QdrantClient:
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=60
    )

    collections = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME not in collections:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=EMBEDDING_DIM,
                distance=Distance.COSINE
            )
        )
    return client


def get_vector_store(client: QdrantClient) -> QdrantVectorStore:
    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=GeminiEmbedder()
    )



def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_documents(docs)


def process_pdf(file) -> List:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.getvalue())
        loader = PyPDFLoader(tmp.name)
        docs = loader.load()

    for d in docs:
        d.metadata.update({
            "source": file.name,
            "type": "pdf",
            "timestamp": datetime.utcnow().isoformat(),
            "hash": sha256(d.page_content)
        })

    return split_docs(docs)


def process_url(url: str) -> List:
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("content", "main", "article", "post")
            )
        )
    )
    docs = loader.load()

    for d in docs:
        d.metadata.update({
            "source": url,
            "type": "url",
            "timestamp": datetime.utcnow().isoformat(),
            "hash": sha256(d.page_content)
        })

    return split_docs(docs)



def query_rewriter() -> Agent:
    return Agent(
        name="QueryRewriter",
        model=Gemini(id="gemini-exp-1206"),
        instructions="""
Rewrite the query to be explicit, detailed, and retrieval-optimized.
Return ONLY the rewritten query.
"""
    )


def rag_agent() -> Agent:
    return Agent(
        name="RAGAgent",
        model=Gemini(id="gemini-2.0-flash-thinking-exp-01-21"),
        instructions="""
SYSTEM RULES:
- Use ONLY the provided context.
- If the answer is missing, say: "Insufficient information."
- Do NOT hallucinate or use outside knowledge.
"""
    )


def web_agent(domains: List[str]) -> Agent:
    return Agent(
        name="WebSearch",
        model=Gemini(id="gemini-exp-1206"),
        tools=[ExaTools(
            api_key=EXA_API_KEY,
            include_domains=domains,
            num_results=5
        )]
    )


st.set_page_config(page_title="Gemini Agentic RAG", layout="wide")
st.title("🤖 Gemini Agentic RAG (Production-Ready)")

client = init_qdrant()
store = get_vector_store(client)

# Sidebar
st.sidebar.header("📥 Knowledge Base")
pdf = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
url = st.sidebar.text_input("Add URL")

use_web = st.sidebar.checkbox("Enable Web Search Fallback", value=True)
domains = st.sidebar.text_input(
    "Search Domains",
    "arxiv.org,wikipedia.org,github.com"
).split(",")

threshold = st.sidebar.slider("Similarity Threshold", 0.0, 1.0, 0.7)

# Ingestion
if pdf:
    docs = process_pdf(pdf)
    store.add_documents(docs)
    st.sidebar.success("PDF ingested")

if url:
    docs = process_url(url)
    store.add_documents(docs)
    st.sidebar.success("URL ingested")

# Chat
query = st.chat_input("Ask a question")

if query:
    with st.chat_message("user"):
        st.write(query)

    rewritten = query_rewriter().run(query).content

    retriever = store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 5, "score_threshold": threshold}
    )
    docs = retriever.invoke(rewritten)

    context = "\n\n".join(d.page_content for d in docs)

    if not context and use_web and EXA_API_KEY:
        web = web_agent(domains)
        context = web.run(rewritten).content
        source_note = "🌐 Web Search"
    else:
        source_note = "📚 Knowledge Base"

    prompt = f"""
CONTEXT:
{context}

QUESTION:
{query}
"""

    answer = rag_agent().run(prompt).content

    with st.chat_message("assistant"):
        st.write(answer)
        st.caption(source_note)
