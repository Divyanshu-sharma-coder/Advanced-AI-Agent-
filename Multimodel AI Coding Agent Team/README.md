# 🤖 Multimodal AI Coding Agent Team

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-o3--mini-black?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini-Multimodal-orange?style=for-the-badge)
![E2B](https://img.shields.io/badge/Sandbox-E2B-green?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open--Source-Welcome-brightgreen?style=for-the-badge)

> **A production-ready, open-source Multimodal AI Coding Agent system**  
> designed to generate, validate, and safely execute Python code from **text or images**.

---

## 🚀 About the Project

This project demonstrates how **real-world AI agent systems** should be built —  
with **security, isolation, validation, and extensibility** in mind.

Unlike toy demos, this system includes:

- 🔍 **Vision Agent** → Extracts coding problems from images (Gemini)

- 🧠 **Coding Agent** → Generates optimal Python solutions (OpenAI)

- 🛡️ **AST Safety Layer** → Blocks unsafe imports & functions

- 🧪 **Sandbox Execution** → Secure code execution via E2B

- 📊 **Executor Agent** → Explains execution results & errors

- 🧩 **Extensible Architecture** → Designed for open-source contributions

> ⚠️ Some advanced challenges are **intentionally left open** to encourage meaningful community contributions.

---

# 🧠 Why This Project Exists

Most AI coding tools:

- ❌ Execute unvalidated code

- ❌ Ignore security risks

- ❌ Are not extensible

# This project:

- ✅ Treats LLM output as **untrusted input**

- ✅ Enforces **multi-layer safety**

- ✅ Encourages **open-source collaboration**

---

# 🏗️ Architecture Overview
User (Text / Image) 
    ↓
Vision Agent (Gemini) 
    ↓
Coding Agent (OpenAI) 
    ↓ 
AST Safety Validation 
    ↓ 
Sandbox Execution (E2B) 
    ↓
Executor Agent (Analysis)

---

## 📦 Project Structure
Multimodel AI Coding Agent Team/ 
├── Coding.py         
# Main application 
├── Requirements.txt   
# Dependencies 
├── README.md         
# Project documentation 
└── CONTRIBUTING.md    # Contribution guidelines

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Divyanshu-sharma-coder/Advanced-AI-Agent-.git
cd Advanced-AI-Agent-/Multimodel\ AI\ Coding\ Agent\ Team
```
2️⃣ Install Dependencies

```
pip install -r Requirements.txt
```

3️⃣ Set Environment Variables
```
export OPENAI_API_KEY="your_openai_key"
export GEMINI_API_KEY="your_gemini_key"
export E2B_API_KEY="your_e2b_key"
```

4️⃣ Run the App
```
streamlit run Coding.py
```
## 🛡️ Security Design

This project uses defense-in-depth:
* LLM constrained prompts
* AST-based code inspection
* Disallowed imports & functions
* Execution time limits
* Isolated sandbox execution
* LLM-generated code is NEVER trusted blindly.

# 🚧 Known Limitations & Open Challenges

These are intentional and open for contributors:

Import whitelisting instead of blacklisting
__builtins__ hardening

Infinite loop / memory bomb detection

Async execution & backend decoupling

Corrective retry agent loops

Observability & tracing

If you enjoy solving hard system problems, this repo is for you.
## 🤝 Contributing

We ❤️ contributors!

Please read CONTRIBUTING.md before submitting PRs.

## 👨‍💻 Author

Divyanshu Sharma

* 🔗 GitHub: @Divyanshu-sharma-coder
* 🌍 Open Source • Built for the Community

If this project helped you:

## ⭐ Star the repo

* 🍴 Fork it
* 🧠 Improve it
* 🚀 Share it
* 🏷️ Hashtags (Reach Boost)

#AIEngineering #AgenticAI #MultimodalAI #OpenSource
#Python #LLM #GenerativeAI #AIProjects
#Streamlit #SecurityEngineering #DevCommunity
