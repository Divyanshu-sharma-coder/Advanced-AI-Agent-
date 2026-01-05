# 🐙 GitHub MCP Agent  
### Explore GitHub Repositories using Natural Language

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=flat-square" />
  <img src="https://img.shields.io/badge/AI-Agent-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/MCP-Model%20Context%20Protocol-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat-square" />
  <img src="https://img.shields.io/github/stars/Divyanshu-sharma-coder/GitHub-MCP-Agent?style=flat-square" />
</p>

<p align="center">
  <b>An AI-powered GitHub analysis agent built using MCP (Model Context Protocol)</b><br>
  Query issues, pull requests, and repository health using natural language — backed by verifiable GitHub data.
</p>

---

## 🚀 Features

✅ Natural language GitHub exploration  
✅ Official **GitHub MCP Server** via Docker  
✅ Zero hallucinations (data-only responses)  
✅ Agent-based reasoning (Agno)  
✅ Clean Streamlit UI  
✅ Dev & Production modes  
✅ Safe, structured, verifiable outputs  

---

## 🧠 How It Works

```text
User Query
   ↓
AI Agent (Agno)
   ↓
MCP Tools (GitHub MCP Server)
   ↓
GitHub API (Issues / PRs / Repos)
   ↓
Structured, Verifiable Insights
```

* Uses GitHub MCP to expose GitHub as structured tools

* AI agent interprets queries and calls only valid MCP tools

* No scraping, no guessing, no hallucinations

* Results are formatted as clean Markdown & tables

## TECH STACK
| Layer | Technology | Purpose |
|------|-----------|--------|
| UI | Streamlit | Interactive web interface |
| Agent Framework | Agno | Agent orchestration & reasoning |
| Protocol | MCP (Model Context Protocol) | Structured tool-based context exchange |
| GitHub Access | GitHub MCP Server | Official GitHub API exposure via MCP |
| LLM | OpenAI (o3-mini) | Natural language understanding & reasoning |
| Container Runtime | Docker | Runs GitHub MCP server |
| Language | Python 3.10+ | Core implementation language |
| Caching | Streamlit Cache | Reduces redundant executions |
| Security | Environment Variables | Secure credential management |


## 🖥️ Demo Queries

Try asking things like:

“Show open issues with recent discussion”

“Which PRs need review?”

“Analyze repository health and maintenance”

“Summarize contributor activity”

## 📦 Installation

1️⃣ Clone the repository
```Bash
git clone https://github.com/Divyanshu-sharma-coder/GitHub-MCP-Agent.git
cd 'GITHUB MCP AGENT'
```
2️⃣ Install dependencies
```Bash
pip install -r requirements.txt
```
3️⃣ System Requirements
```
* Python 3.10+
* Docker (required for GitHub MCP server)
* Verify Docker:
docker --version
```

## 🔐 Configuration

Development Mode (Local)
API keys can be entered directly in the UI.
Production Mode (Recommended)
Set environment variables:

```Bash
export OPENAI_API_KEY=your_openai_key
export GITHUB_TOKEN=your_github_token
export APP_MODE=prod
```
* ⚠️ GitHub token must have repo scope.

▶️ Run the App

```Bash
streamlit run app.py
```
Open in browser:
```
http://localhost:8501
```
## 🛡️ Security Principles

* No credentials committed to code
* Secrets via environment variables
* MCP ensures data integrity
* AI agent restricted to tool outputs only
* No speculative or fabricated answers

## ⚠️ Known Limitations
* Docker container starts per query (cold start latency)
* GitHub API rate limits apply
* Designed for analysis, not mutation (read-only)
* These are intentional tradeoffs for safety and correctness.

## 🤝 Contributing

Contributions are welcome 🚀
If you want to improve performance, UX, or add new MCP toolsets:
👉 See CONTRIBUTING.md
Pull Requests are appreciated!

## 📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

## ⭐ Support the Project
If you find this useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Open a discussion
* 🔧 Submit a PR

## 👨‍💻 Author

Divyanshu Sharma

AI Engineer | Agent Systems | MCP Enthusiast
* 🔗 GitHub: https://github.com/Divyanshu-sharma-coder
* 🔗 LinkedIn: https://www.linkedin.com/in/divyanshu-jyotishi-17729036b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
