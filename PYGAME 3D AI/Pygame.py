import streamlit as st
from openai import OpenAI
from agno.agent import Agent as AgnoAgent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat as AgnoOpenAIChat
from langchain_openai import ChatOpenAI 
import asyncio
from browser_use import Browser

st.set_page_config(page_title="PyGame Code Generator", layout="wide")

# Initialize session state
if "api_keys" not in st.session_state:
    st.session_state.api_keys = {
                        await coder.run()
                        await viewer.run()
                    except Exception as e:
                        st.error(f"Error running code on Trinket: {str(e)}")

        # Run the async function with the stored code
        asyncio.run(run_pygame_on_trinket(st.session_state.generated_code))

elif generate_code_btn and not query:
    st.warning("Please enter a query before generating code")                        st.info("You can still copy the code above and run it manually on Trinket")
                        st.success("Code is running on Trinket!")
                        await executor.run()
                    try:
                        await agent1.run()

                with st.spinner("Running code on Trinket..."):
        "deepseek": "",
                    browser_context=context,
                )
        "openai": ""
    }
                    task='Viewer. Your job is to just view the pygame window for 10 seconds.',
                    llm=model,

# Streamlit sidebar for API keys
with st.sidebar:
    st.title("API Keys Configuration")
                
                viewer = Agent(
    st.session_state.api_keys["deepseek"] = st.text_input(
        "DeepSeek API Key",
        type="password",
                )
        value=st.session_state.api_keys["deepseek"]
    )
                    browser_context=context
    st.session_state.api_keys["openai"] = st.text_input(
                    llm=model,
        "OpenAI API Key",
        type="password",
        value=st.session_state.api_keys["openai"]
    )
                coder = Agent(
                    task='Coder. Your job is to wait for the user for 10 seconds to write the code in the code editor.',
    
    st.markdown("---")

    st.info("""
    📝 How to use:
    1. Enter your API keys above
                )
    2. Write your PyGame visualization query
    3. Click 'Generate Code' to get the code
    4. Click 'Generate Visualization' to:
                    browser_context=context
       - Open Trinket.io PyGame editor
       - Copy and paste the generated code
       - Watch it run automatically
    """)
                    llm=model,

# Main UI
st.title("🎮 AI 3D Visualizer with DeepSeek R1")
example_query = "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
query = st.text_area(
    "Enter your PyGame query:",
    height=70,
    placeholder=f"e.g.: {example_query}"
)

# Split the buttons into columns
                executor = Agent(
                    task='Executor. Execute the code written by the User by clicking on the run button on the right. ',
col1, col2 = st.columns(2)
generate_code_btn = col1.button("Generate Code")
generate_vis_btn = col2.button("Generate Visualization")
                

if generate_code_btn and query:
    if not st.session_state.api_keys["deepseek"] or not st.session_state.api_keys["openai"]:
                )
        st.error("Please provide both API keys in the sidebar")
        st.stop()

                    browser_context=context,
    # Initialize Deepseek client
    deepseek_client = OpenAI(
        api_key=st.session_state.api_keys["deepseek"],
                    llm=model,
        base_url="https://api.deepseek.com"
    )

                    task='Go to https://trinket.io/features/pygame, thats your only job.',
    system_prompt = """You are a Pygame and Python Expert that specializes in making games and visualisation through pygame and python programming. 
    During your reasoning and thinking, include clear, concise, and well-formatted Python code in your reasoning. 
    Always include explanations for the code you provide."""
                agent1 = Agent(

    try:
        with st.spinner("Extracting code..."):
                
            code_response: RunOutput = openai_agent.run(extraction_prompt)
        st.session_state.generated_code = extracted_code
        
                )
        # Display the code
        with st.expander("Generated PyGame Code", expanded=True):      
            st.code(extracted_code, language="python")
            
                    api_key=st.session_state.api_keys["openai"]
        st.success("Code generated successfully! Click 'Generate Visualization' to run it.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

                    model="gpt-4o", 
elif generate_vis_btn:
    if "generated_code" not in st.session_state:
        st.warning("Please generate code first before visualization")
    else:
        async def run_pygame_on_trinket(code: str) -> None:
            browser = Browser()
            from browser_use import Agent 
            async with await browser.new_context() as context:
                model = ChatOpenAI(
        # Store the generated code in session state
            extracted_code = code_response.content


