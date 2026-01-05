from __future__ import annotations

import asyncio
import os
import shutil
import streamlit as st
from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters

# APP CONFIG

st.set_page_config(
    page_title="🐙 GitHub MCP Agent",
    page_icon="🐙",
    layout="wide"
)

APP_MODE = os.getenv("APP_MODE", "dev")  # dev | prod
REQUEST_TIMEOUT = 120

# SECURITY HELPERS

def require_env(var: str) -> str:
    value = os.getenv(var)
    if not value:
        st.error(f"❌ Server misconfiguration: `{var}` not set")
        st.stop()
    return value

def docker_available() -> bool:
    return shutil.which("docker") is not None

def validate_repo(repo: str) -> bool:
    parts = repo.split("/")
    return len(parts) == 2 and all(parts)

# HEADER

st.markdown("<h1>🐙 GitHub MCP Agent</h1>", unsafe_allow_html=True)
st.markdown(
    "Explore GitHub repositories using **natural language**, powered by "
    "**MCP (Model Context Protocol)** and **agent-based reasoning**."
)

# AUTHENTICATION

with st.sidebar:
    st.header("🔐 Authentication")

    if APP_MODE == "dev":
        openai_key = st.text_input("OpenAI API Key", type="password")
        github_token = st.text_input("GitHub Token", type="password")

        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if github_token:
            os.environ["GITHUB_TOKEN"] = github_token
    else:
        require_env("OPENAI_API_KEY")
        require_env("GITHUB_TOKEN")

    st.markdown("---")
    st.caption("🔒 In production mode, secrets must be provided via environment variables only.")

# INPUT CONTROLS

col1, col2 = st.columns([3, 1])

with col1:
    repo = st.text_input(
        "Repository",
        placeholder="owner/repo",
        help="Example: openai/openai-cookbook"
    )

with col2:
    query_type = st.selectbox(
        "Query Type",
        ["Issues", "Pull Requests", "Repository Analysis", "Custom"]
    )

QUERY_TEMPLATES = {
    "Issues": "Show open issues with labels and recent discussion",
    "Pull Requests": "List pull requests that need review",
    "Repository Analysis": "Analyze repository health, activity, and maintenance",
    "Custom": ""
}

query = st.text_area(
    "Your Query",
    value=QUERY_TEMPLATES.get(query_type, ""),
    placeholder="Ask something meaningful about the repository"
)

# CORE EXECUTION

@st.cache_data(ttl=300, show_spinner=False)
def cached_run(repo: str, query: str) -> str:
    return asyncio.run(run_agent(repo, query))

async def run_agent(repo: str, query: str) -> str:
    if not docker_available():
        return "❌ Docker is required to run the GitHub MCP server."

    openai_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")

    if not openai_key or not github_token:
        return "❌ Missing API keys."

    server_params = StdioServerParameters(
        command="docker",
        args=[
            "run", "-i", "--rm",
            "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
            "-e", "GITHUB_TOOLSETS",
            "ghcr.io/github/github-mcp-server"
        ],
        env={
            "GITHUB_PERSONAL_ACCESS_TOKEN": github_token,
            "GITHUB_TOOLSETS": "repos,issues,pull_requests"
        }
    )

    async with MCPTools(server_params=server_params) as mcp_tools:
        agent = Agent(
            tools=[mcp_tools],
            instructions=dedent("""
                You are a GitHub analysis agent.

                RULES:
                - Use ONLY data returned by GitHub MCP tools
                - NEVER speculate or hallucinate
                - If data is unavailable, say so explicitly
                - Prefer tables for structured data
                - Include direct GitHub links when relevant
                - Be concise, factual, and structured
            """),
            markdown=True,
        )

        full_query = f"{query} in {repo}"
        response: RunOutput = await asyncio.wait_for(
            agent.arun(full_query),
            timeout=REQUEST_TIMEOUT
        )
        return response.content

# EXECUTION BUTTON

if st.button("🚀 Run Query", type="primary", use_container_width=True):
    if not validate_repo(repo):
        st.error("❌ Invalid repository format. Use `owner/repo`.")
    elif not query.strip():
        st.error("❌ Please enter a query.")
    else:
        with st.spinner("🔍 Analyzing repository..."):
            result = cached_run(repo, query)

        st.markdown("### 📊 Results")
        st.markdown(result)

# FOOTER INFO

if not st.session_state.get("ran", False):
    st.markdown(
        """
        ### ℹ️ How this works
        - Uses **GitHub MCP Server** (official) via Docker
        - MCP exposes GitHub as structured tools
        - An AI agent interprets your query and calls tools
        - Results are returned as **verifiable GitHub data**
        
        **Tech Stack**
        - 🧠 Agent Framework: Agno
        - 🔌 MCP: Model Context Protocol
        - 🐙 GitHub MCP Server
        - 🧩 OpenAI Models
        - 🖥️ Streamlit UI
        """
    )
