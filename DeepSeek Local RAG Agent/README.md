# 🐋 DeepSeek Local RAG Reasoning Agent

Built & Maintained by Divyanshu Jyotishi

📂 Repo: Advanced-AI-Agent-


---

* A powerful local RAG + reasoning agent that combines DeepSeek local models (via Ollama), Snowflake embeddings, Qdrant vector DB, and a clean agentic architecture.
This agent supports local-only chat, RAG-enhanced reasoning, PDF/document intelligence, and web search fallback, all wrapped inside a Streamlit interface.


---

# 🚀 Features

🔹 Dual Modes

Local Chat Mode → Pure DeepSeek local reasoning

RAG Mode → DeepSeek + document context + web search (llama3.2)



---

# 📄 RAG Document Intelligence

PDF upload & text extraction

Web page scraping

Auto chunking + embedding (Snowflake Arctic Embed)

Vector storage in Qdrant Cloud



---

# 🧠 Smart Querying (RAG Mode)

RAG-based retrieval

Threshold similarity filtering

Automatic fallback to Exa Web Search

Source citations



---

# ⚙️ Advanced Capabilities

Exa AI search integration

Domain-filtered search

Chat history memory

"Thinking Process" visualization

Model switching on the fly



---

# 🧩 Supported Models
```
deepseek-r1:1.5b (lightweight, laptop-friendly)

deepseek-r1:7b (better reasoning)

snowflake-arctic-embed (SOTA embeddings)

llama3.2 (web search & fallback reasoning)
```


---

# 🛠️ Prerequisites

1️⃣ Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```
Pull required models
```
ollama pull deepseek-r1:1.5b
ollama pull deepseek-r1:7b
ollama pull snowflake-arctic-embed
ollama pull llama3.2
```

---

2️⃣ Qdrant Cloud Setup (for RAG Mode)

Create an account

Make a new cluster

Get:
```
QDRANT_API_KEY

QDRANT_URL
```



---

3️⃣ Exa AI API Key (Optional but Recommended)
```
Sign up → generate API key

Enables web search fallback
```


---

# ▶️ How to Run (Repo Version)

Step 1: Go to your repo
```
cd ~/Advanced-AI-Agent-
cd "DeepSeek Local RAG Agent"
```
Step 2: Install dependencies
```
pip install -r Requirement.txt
```
Step 3: Run the agent
```
streamlit run RagAgent.py
```
---

# 📦 Project Structure
```
Advanced-AI-Agent-/
│
├── AI Meeting Agent/
│
├── AI System Architect Agent/
│
├── MultiModel UIUX Feedback Agent Team With Nano Banana/
│
└── DeepSeek Local RAG Agent/
      ├── RagAgent.py
      ├── Requirement.txt
      └── README.md
```


# 🚀 How to Use This Repository

Follow these steps to set up and run the DeepSeek Local RAG Reasoning Agent on your own system.


---

📥 1. Clone the Repository
```
git clone https://github.com/Divyanshu-sharma-coder/DeepSeek-Local-RAG-Agent.git
```
Then move into the folder:
```
cd DeepSeek-Local-RAG-Agent
```

---

📦 2. Install Dependencies

Ensure Python 3.10+ is installed.

Install required packages:
```
pip install -r requirements.txt
```

---

🧠 3. Install Required Ollama Models

You must install DeepSeek locally using Ollama.

Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```
Pull the required models
```
# Lightweight model (works on most laptops)
ollama pull deepseek-r1:1.5b

# Heavier reasoning model
ollama pull deepseek-r1:7b

# Embedding model for RAG
ollama pull snowflake-arctic-embed

# Backup model for web search fallback
ollama pull llama3.2
```

---

🗂️ 4. Configure Qdrant (Required for RAG Mode)

Create a cluster at Qdrant Cloud, then add your credentials.

Create an .env file:
```
nano .env
```
Add:
```
QDRANT_URL=your_cluster_url
QDRANT_API_KEY=your_api_key
EXA_API_KEY=optional_exa_key
```
Save & exit.


---

▶️ 5. Run the Application
```
streamlit run RagAgent.py
```
The app will open in your browser with:

Local Chat Mode

Full RAG Mode

Document uploads

Web search integration

Thinking process visualization



---

# 🙋 How Others Can Use This Repo

Anyone can run your agent by following these steps:

1. Clone the repo


2. Install dependencies


3. Install DeepSeek + Embedding models in Ollama


4. Set up Qdrant (only if using RAG mode)


5. Run the Streamlit interface



