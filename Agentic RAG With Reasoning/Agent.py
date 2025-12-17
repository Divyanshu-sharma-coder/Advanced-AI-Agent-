import os
import json
import streamlit as st
from dotenv import load_dotenv
from typing import Dict, Any

from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools


# Environment & App Config


load_dotenv()

st.set_page_config(
    page_title="Elite Agentic RAG",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Elite Agentic RAG (Corrective & Self-Reflective)")


# API Keys

st.subheader("🔑 API Keys")

google_key = st.text_input(
    "Google API Key (Gemini)",
    type="password",
    value=os.getenv("GOOGLE_API_KEY", "")
)

openai_key = st.text_input(
    "OpenAI API Key (Embeddings)",
    type="password",
    value=os.getenv("OPENAI_API_KEY", "")
)

if not (google_key and openai_key):
    st.info("Enter both API keys to continue.")
    st.stop()


# Utilities (Robust Parsing)


def safe_json(text: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    return fallback


# Knowledge Base


@st.cache_resource(show_spinner="📚 Initializing Knowledge Base...")
def load_knowledge() -> Knowledge:
    return Knowledge(
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="elite_rag_docs",
            search_type=SearchType.vector,
            embedder=OpenAIEmbedder(api_key=openai_key),
        )
    )

knowledge = load_knowledge()

# Knowledge Sources


if "urls" not in st.session_state:
    st.session_state.urls = [
        "https://www.theunwindai.com/p/mcp-vs-a2a-complementing-or-supplementing"
    ]

if "loaded_urls" not in st.session_state:
    st.session_state.loaded_urls = set()

with st.sidebar:
    st.header("📚 Knowledge Sources")
    for url in st.session_state.urls:
        st.write(f"• {url}")

    new_url = st.text_input("Add URL")
    if st.button("➕ Add URL") and new_url:
        if new_url not in st.session_state.urls:
            st.session_state.urls.append(new_url)
        st.rerun()

for url in st.session_state.urls:
    if url not in st.session_state.loaded_urls:
        knowledge.add_content(url=url)
        st.session_state.loaded_urls.add(url)


# Agents (STRICT CONTRACTS)

def build_agents(kb: Knowledge) -> Dict[str, Agent]:

    planner = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=google_key),
        instructions=[
            "Return ONLY valid JSON.",
            "Schema: {need_retrieval: bool, k: int, focus: string}",
        ],
    )

    retriever = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=google_key),
        knowledge=kb,
        search_knowledge=True,
        instructions=[
            "Retrieve ONLY relevant context.",
            "Do not answer the question.",
        ],
    )

    reasoner = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=google_key),
        tools=[ReasoningTools(add_instructions=True)],
        instructions=[
            "Answer ONLY using provided context.",
            "Cite sources.",
        ],
        markdown=True,
    )

    verifier = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=google_key),
        instructions=[
            "Return JSON only.",
            "Schema: {supported: bool, issues: list}",
        ],
    )

    reflector = Agent(
        model=Gemini(id="gemini-2.5-flash", api_key=google_key),
        instructions=[
            "Return JSON only.",
            "Schema: {confidence: float, explanation: string}",
        ],
    )

    return {
        "planner": planner,
        "retriever": retriever,
        "reasoner": reasoner,
        "verifier": verifier,
        "reflector": reflector,
    }

agents = build_agents(knowledge)


# Query Section

st.divider()
query = st.text_area(
    "Ask a question",
    value="What is the difference between MCP and A2A protocols?",
)

MAX_RETRIES = 2

if st.button("🚀 Run Elite Agentic RAG"):
    with st.spinner("🧠 Agents thinking..."):

        final_answer = None
        final_confidence = 0.0
        citations = []

        for _ in range(MAX_RETRIES + 1):

            # 1️⃣ Planner
            plan_raw = agents["planner"].run(query).content
            plan = safe_json(
                plan_raw,
                {"need_retrieval": True, "k": 4, "focus": ""},
            )

            retrieved_context = ""

            # 2️⃣ Retrieval
            if plan.get("need_retrieval", True):
                retrieval = agents["retriever"].run(
                    f"Retrieve top {plan['k']} documents.\n"
                    f"Query: {query}\n"
                    f"Focus: {plan.get('focus','')}"
                )
                retrieved_context = retrieval.content
                if retrieval.citations:
                    citations = retrieval.citations.urls

            # 3️⃣ Reasoning
            answer = agents["reasoner"].run(
                f"Question:\n{query}\n\nContext:\n{retrieved_context}"
            )

            # 4️⃣ Verification
            verify_raw = agents["verifier"].run(answer.content).content
            verdict = safe_json(verify_raw, {"supported": False})

            if not verdict.get("supported", False):
                continue

            # 5️⃣ Reflection
            reflect_raw = agents["reflector"].run(answer.content).content
            reflection = safe_json(reflect_raw, {"confidence": 0.0})

            final_confidence = reflection.get("confidence", 0.0)

            if final_confidence >= 0.75:
                final_answer = answer.content
                break

        # Output

        if final_answer:
            st.success("✅ High-confidence answer generated")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 💡 Answer")
                st.markdown(final_answer)

            with col2:
                st.markdown("### 📊 Confidence")
                st.metric("Score", f"{final_confidence:.2f}")

            if citations:
                st.markdown("### 📚 Sources")
                for c in citations:
                    st.markdown(f"- [{c.title or c.url}]({c.url})")
        else:
            st.error("❌ Failed to reach confident answer after retries")

