"""
Production-Ready Multimodal AI Coding Agent

Author: Divyanshu Sharma
"""

from __future__ import annotations
from typing import Optional
import os
import tempfile
import logging
import ast
import streamlit as st
from pathlib import Path
from PIL import Image

from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.media import Image as AgnoImage
from e2b_code_interpreter import Sandbox

# LOGGING

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# CONFIGURATION

EXECUTION_TIMEOUT = 30
SANDBOX_TIMEOUT = 60

DISALLOWED_IMPORTS = {
    "os", "sys", "subprocess", "socket", "shutil",
    "pathlib", "multiprocessing", "threading"
}

# SECURITY: ENV ONLY

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
E2B_KEY = os.getenv("E2B_API_KEY")

if not all([OPENAI_KEY, GEMINI_KEY, E2B_KEY]):
    st.error("❌ Missing API keys. Set them as environment variables.")
    st.stop()

# AGENT FACTORY

@st.cache_resource
def create_agents() -> tuple[Agent, Agent, Agent]:
    vision = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=GEMINI_KEY),
        markdown=True,
    )

    coder = Agent(
        model=OpenAIChat(
            id="o3-mini",
            api_key=OPENAI_KEY,
            system_prompt=(
                "You are a senior Python engineer. "
                "Generate ONLY one executable Python code block. "
                "No explanations outside the code."
            ),
        ),
        markdown=True,
    )

    executor = Agent(
        model=OpenAIChat(
            id="o3-mini",
            api_key=OPENAI_KEY,
            system_prompt=(
                "You analyze Python execution results. "
                "Explain outputs or errors clearly and concisely."
            ),
        ),
        markdown=True,
    )

    return vision, coder, executor

# CODE SAFETY LAYER

def validate_code_safety(code: str) -> Optional[str]:
    """AST-based validation for unsafe code."""
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"Syntax Error: {e}"

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                if alias.name.split(".")[0] in DISALLOWED_IMPORTS:
                    return f"Disallowed import detected: {alias.name}"

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in {"exec", "eval", "compile"}:
                return f"Disallowed function call: {node.func.id}"

    return None

# UTILS

def extract_python_code(markdown: str) -> Optional[str]:
    import re
    match = re.search(r"```python(.*?)```", markdown, re.DOTALL)
    return match.group(1).strip() if match else None

def analyze_image(agent: Agent, image: Image.Image) -> str:
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        image.convert("RGB").save(tmp.name)
        agno_img = AgnoImage(filepath=Path(tmp.name))

    try:
        response: RunOutput = agent.run(
            "Extract the coding problem clearly.",
            images=[agno_img],
        )
        return response.content
    finally:
        os.remove(tmp.name)

def execute_safely(
    executor_agent: Agent,
    code: str
) -> str:
    """Run code safely and explain results."""
    with Sandbox(timeout=SANDBOX_TIMEOUT) as sandbox:
        sandbox.set_timeout(EXECUTION_TIMEOUT)
        result = sandbox.run_code(code)

        prompt = f"""
Execution Logs:
{result.logs}

Execution Error:
{result.error}
"""

        analysis: RunOutput = executor_agent.run(prompt)
        return analysis.content

# UI

def main():
    st.set_page_config(page_title="AI Coding Agent", layout="centered")
    st.title("🤖 Multimodal AI Coding Agent")

    vision, coder, executor = create_agents()

    uploaded = st.file_uploader("Upload problem image", type=["png", "jpg"])
    query = st.text_area("Or describe the problem")

    if st.button("Generate & Execute", type="primary"):
        if uploaded:
            logging.info("Image input received")
            problem = analyze_image(vision, Image.open(uploaded))
            st.info(problem)
        elif query:
            logging.info("Text input received")
            problem = query
        else:
            st.warning("Provide input")
            return

        with st.spinner("Generating code..."):
            solution: RunOutput = coder.run(problem)

        code = extract_python_code(solution.content)
        if not code:
            st.error("❌ No executable Python code generated.")
            return

        st.code(code, "python")

        logging.info("Validating generated code")
        violation = validate_code_safety(code)
        if violation:
            logging.warning(f"Blocked unsafe code: {violation}")
            st.error(f"🚫 Code blocked: {violation}")
            return

        with st.spinner("Executing safely..."):
            result = execute_safely(executor, code)

        st.markdown("### 🚀 Execution Analysis")
        st.markdown(result)

if __name__ == "__main__":
    main()
