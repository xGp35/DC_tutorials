"""
ReAct demo: LangChain + HuggingFace text-generation model + wikipedia tool.

This script:
- creates a Hugging Face text-generation pipeline
- wraps it in LangChain's HuggingFacePipeline LLM wrapper
- loads the wikipedia tool
- initializes a ReAct-style agent (ZERO_SHOT_REACT_DESCRIPTION)
- runs a single query and prints the agent output

Notes:
- Model: crumb/nano-mistral in the example; replace with any other HF model id if you prefer.
- The wikipedia tool fetches and summarizes pages; the agent will decide when to call it.
"""
from langchain import hub
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv
import os
load_dotenv()  # loads .env into environment variables

hf_token = os.getenv("HUGGING_FACE_READ_TOKEN")


# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_agent(llm, tools).bind_tools(tools)

print("Sending query to agent...")
# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response)
