# 🤖 Gemini Agentic RAG

An **Agentic Retrieval-Augmented Generation (RAG)** system powered by **Gemini 2.0 Flash Thinking**, designed for intelligent reasoning, adaptive retrieval, and extensibility.

This project is part of the **Advanced-AI-Agent** open-source collection by  
**Divyanshu Sharma** (GitHub: @Divyanshu-sharma-coder).

---

## 🚀 Overview

**Gemini Agentic RAG** is not a basic RAG pipeline.

It is a **modular, agent-driven RAG framework** that combines:
- Query reformulation
- Vector-based retrieval
- Context-aware reasoning
- Web search fallback
- Agent orchestration

The system is intentionally designed with **clear extension points** so developers can customize, experiment, and productionize it in their own way.

---

## 🧠 Architecture
```
User Query 
   ↓
Query Rewriter Agent 
   ↓ 
Vector Retrieval (Qdrant)
   ↓
Context Builder
   ↓
Gemini Flash Thinking RAG Agent 
   ↓ 
(Optional) Web Search Agent (Exa)
```

---

## ✨ Key Features

### 🔍 Agentic Retrieval
- Query rewriting for retrieval optimization
- Similarity-based document retrieval
- Score threshold filtering

### 📚 Knowledge Sources
- PDF document ingestion
- Web page ingestion
- Automatic chunking & embedding
- Vector storage using **Qdrant Cloud**

### 🌐 Web Search Fallback
- Exa AI integration
- Domain-restricted search
- Used only when internal knowledge is insufficient

### 🧠 Reasoning & Safety
- Gemini 2.0 Flash Thinking for reasoning
- Strict hallucination control
- Context-only answering policy

### 🛠 Developer-Friendly
- Modular agents
- Clear extension points
- Streamlit UI for rapid experimentation

---

## 🧩 Tech Stack

| Component | Technology |
|--------|-----------|
| LLM | Gemini 2.0 Flash Thinking |
| Embeddings | Gemini Embedding Model |
| Vector DB | Qdrant |
| Agent Framework | Agno (Phidata) |
| Web Search | Exa AI |
| UI | Streamlit |
| Language | Python |

---

## 📂 Project Structure
```
Gemini Agentic RAG/ 
├── GEMINI.py          # Core application 
├── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Divyanshu-sharma-coder/Advanced-AI-Agent.git
cd "Advanced-AI-Agent/Gemini Agentic RAG"
```

2️⃣ Install dependencies


```
pip install -r requirements.txt
```
3️⃣ Set environment variables

```
export GOOGLE_API_KEY="your_key"
export QDRANT_API_KEY="your_key"
export QDRANT_URL="your_url"
export EXA_API_KEY="your_key"

```
4️⃣ Run the app
```

streamlit run GEMINI.py
```
# 🔧 Customization & Extension Points

This project is intentionally designed to be extended.
You can easily add:

🔁 Rerankers (cross-encoder, LLM-based)

⚡ Async ingestion pipelines

🧪 RAG evaluation (RAGAS, custom metrics)

🔐 Authentication & user isolation

📊 Observability & logging

🚀 FastAPI backend instead of Streamlit

* See CONTRIBUTING.md for guidance.

# 🗺️ Roadmap

[ ] Reranking support

[ ] FastAPI backend

[ ] Async ingestion workers

[ ] Answer verification agent

[ ] RAG evaluation pipeline

[ ] Observability & tracing

# 🤝 Contributing

Contributions are welcome and encouraged 🚀
Please read CONTRIBUTING.md before submitting a PR.

# 🙌 Author

* Divyanshu Sharma
* AI Engineer | Agentic Systems | RAG Architect
* GitHub: @Divyanshu-sharma-coder
If you find this project useful, ⭐ the repo!
