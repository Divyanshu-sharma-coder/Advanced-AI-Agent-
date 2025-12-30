---

# 🧩 `CONTRIBUTING.md`


# 🤝 Contributing Guidelines

Thank you for considering contributing to **Multimodal AI Coding Agent Team** 🎉  
This project is designed as a **production-grade core** and welcomes serious, meaningful contributions.

---

## 🧠 Philosophy

- LLM output is **untrusted**
- Security > convenience
- Clean architecture > hacks
- Contributions should **strengthen the system**

---

## ✅ What You Can Contribute

We actively welcome PRs in these areas:

### 🔒 Security & Safety
- Import whitelisting
- `__builtins__` restriction
- Sandbox escape prevention
- Memory & CPU bomb detection

### 🏗️ Architecture
- FastAPI backend refactor
- Async execution pipelines
- Multi-user isolation
- WebSocket streaming

### 🤖 AI System Enhancements
- Auto test-case generation
- Corrective execution loops
- Failure-aware retry agents
- Confidence scoring

### 📊 Observability
- Structured logging
- Tracing (OpenTelemetry)
- Execution metrics

---

## 🛠️ How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
  ```
3. Write clean, documented code
4. Test your changes
5. Submit a Pull Request

# 📐 Code Standards
Python 3.10+

Type hints required

Clear function docstrings

No unnecessary dependencies

Security-first mindset

## ❌ What Will Be Rejected

Blind execution of LLM output

Hardcoded API keys

Unscoped refactors

Breaking architecture contracts

Low-effort or cosmetic PRs

## 🧪 Testing Expectations

If your PR:
Affects execution → add safety checks
Affects agents → update prompts
Affects security → explain threat model

## 💬 Discussions
If unsure:
Open an Issue
Propose your approach
Discuss before coding

## 🧠 Final Note

This project is not a beginner toy.
It is meant for developers who enjoy thinking deeply about systems.
If that excites you — welcome aboard 🚀
