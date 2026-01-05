# 🤝 Contributing to GitHub MCP Agent

First of all, thank you for taking the time to contribute!  
This project is built to encourage **high-quality, well-reasoned contributions** around AI agents, MCP, and GitHub tooling.

---

## 🎯 Project Philosophy

This project follows a few core principles:

- ✅ **Verifiable data only** (no hallucinations)
- ✅ **Agent-first architecture**
- ✅ **Security by default**
- ✅ **Readable, maintainable code**
- ✅ **Minimal dependencies**

Please keep these principles in mind when contributing.

---

## 🧠 Ways to Contribute

You can help in many ways:

- 🐛 Fix bugs or edge cases
- 🚀 Improve performance or UX
- 🧩 Add new MCP toolsets (e.g. commits, discussions)
- 🧪 Improve error handling and validation
- 📚 Improve documentation
- 🎨 UI/UX improvements (Streamlit)

---

## 🛠️ Development Setup

### 1️⃣ Fork & Clone
```bash
git clone https://github.com/Divyanshu-sharma-coder/GitHub-MCP-Agent.git
cd GitHub-MCP-Agent

###2️⃣ Create a Virtual Environment
```python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

###3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
###4️⃣ System Requirements
* Python 3.10+
* Docker (required for GitHub MCP server)

## 🔐 Environment Variables
```
Create a .env file or export variables:
```
```Bash
export OPENAI_API_KEY=your_openai_key
export GITHUB_TOKEN=your_github_token
export APP_MODE=dev
```
##⚠️ Never commit secrets.
The .gitignore already excludes .env files.

###▶️ Running the App
```
streamlit run app.py
```
##🧪 Testing Guidelines
* This project currently relies on manual testing.
* When submitting PRs:
* Test with at least one public repository
* Verify issue and PR queries work
* Confirm no hallucinated responses
* Ensure Docker container starts correctly
* Automated tests are welcome via PRs.

## 📐 Code Style Guidelines
Please follow these conventions:
* Use type hints wherever possible
* refer pure functions
* Keep functions small and focused
* Avoid hard-coded values
* Log errors clearly
* No silent except: blocks

## 🧠 Agent Rules (Important)
If you modify agent instructions:
* Do not weaken hallucination controls
* Do not allow speculative answers
* MCP tool responses must remain the single source of truth

## 📦 Pull Request Process
Create a feature branch:

```Bash
git checkout -b feature/your-feature-name
```
* Make focused, meaningful commits
* Ensure the app runs without errors
* Open a Pull Request with:
* Clear description
* What problem it solves
* Any trade-offs made
* Low-effort or breaking PRs may be closed.

## 🏷️ Commit Message Convention (Recommended)
```Text
type(scope): short description

Examples:
feat(agent): add repository discussions support
fix(ui): handle invalid repository input
docs(readme): improve setup instructions
```
## 📣 Reporting Issues
If you find a bug:
* Search existing issues first
* Provide clear reproduction steps
* Include screenshots or logs if possible

## 📜 License
By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙌 Final Notes
This project is intentionally clean and minimal.
Every line of code should earn its place.
If you’re unsure about a change — open an issue first.
Thoughtful discussions are always welcome 🚀
Happy contributing!

– Divyanshu Sharma
