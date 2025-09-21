#Over the next couple of exercises, you'll work to create a system for helping people learn new skills. 
# This system needs to be built sequentially, so learners can modify plans based on their preferences and constraints. 
# You'll utilize your LangChain LCEL skills to build a sequential chain to build this system, 
# and the first step is to design the prompt templates that will be used by this system.
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Create a prompt template that takes an input activity
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "Play Golf"}))


#With your prompt templates created, it's time to tie everything together, including the LLM, using chains and LCEL. 
# An llm has already been defined for you that uses OpenAI's gpt-4o-mini model

# For the final step of calling the chain, feel free to insert any activity you wish! If you're struggling for ideas, try inputting "play the harmonica"

learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Complete the sequential chain with LCEL
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "Play Golf"}))