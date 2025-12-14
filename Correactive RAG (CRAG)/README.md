# 🔄 Corrective RAG Agent (CRAG)

A Corrective Retrieval-Augmented Generation (CRAG) system that implements a multi-stage, self-correcting RAG workflow using LangGraph. This agent is designed to go beyond basic RAG by grading retrieved documents, correcting queries when needed, and intelligently falling back to web search to deliver accurate, context-aware answers.

Built and maintained inside the Advanced-AI-Agent- repository by Divyanshu Sharma.


---

# 🚀 Features

# 📄 Smart Document Retrieval

Uses Qdrant as a high-performance vector database

Efficient semantic search over uploaded documents


# ✅ Document Relevance Grading

Uses Claude 4.5 Sonnet to evaluate whether retrieved documents are actually useful

Filters out irrelevant or weak context automatically


# 🔁 Query Transformation (Correction Loop)

Reformulates the user query when retrieval quality is low

Improves downstream search and answer quality


# 🌐 Web Search Fallback

Integrates Tavily API for live web search

Automatically triggered when local knowledge is insufficient


# 🧠 Multi-Model Architecture

OpenAI Embeddings → Vector representations

Claude 4.5 Sonnet → Reasoning, grading, and final generation


# 🖥️ Interactive UI

Built with Streamlit

Upload documents, ask questions, and observe the CRAG workflow step-by-step



---

# ⚙️ How It Works (CRAG Flow)

1. User submits a query


2. Relevant documents are retrieved from Qdrant


3. Claude grades document relevance


4. If relevance is low → query is rewritten


5. Retrieval runs again OR web search is triggered


6. Final grounded response is generated



This ensures higher accuracy, fewer hallucinations, and better coverage.


---

# ▶️ How to Run

1️⃣ Clone the Repository
```
git clone https://github.com/Divyanshu-sharma-coder/Advanced-AI-Agent-.git
cd Advanced-AI-Agent-/Correactive\ RAG\ \(CRAG\)
```

---

2️⃣ Install Dependencies
```
pip install -r Requirements.txt
```

---

3️⃣ Set Up API Keys

You will need the following API keys:

* OpenAI API Key → embeddings

* Anthropic API Key → Claude 4.5 Sonnet

* Tavily API Key → web search

* Qdrant API Key & URL → vector storage


Create a .env file:
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
TAVILY_API_KEY=your_tavily_key
QDRANT_API_KEY=your_qdrant_key
QDRANT_URL=https://your-cluster.cloud.qdrant.io
```

---

4️⃣ Run the Application
```
streamlit run RAG.py
```

---

# 🧰 Tech Stack

LangChain — RAG components & chains

LangGraph — Corrective workflow orchestration

Qdrant — Vector database

Claude 4.5 Sonnet — Reasoning & relevance grading

OpenAI — Embeddings

Tavily — Web search

Streamlit — UI



---

# 📁 Project Structure
```
Advanced-AI-Agent-/
│
├── Correactive RAG (CRAG)/
│   ├── RAG.py
│   ├── Requirements.txt
│   └── README.md

```
---

# 🎯 Use Cases

Reliable document Q&A systems

Enterprise knowledge bases

Research assistants

Hallucination-resistant RAG pipelines

Hybrid local + web intelligence agents



---

# ⚠️ Notes & Limitations

Requires external API keys

Web search depends on Tavily availability

Best results with clean, well-structured documents



---

# ⭐ Part of the Advanced-AI-Agent- collection

A growing repository of production-grade AI agents focused on reasoning, orchestration, and real-world intelligence.
