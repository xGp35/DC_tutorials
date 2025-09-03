from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")
from langchain_core.prompts import PromptTemplate

# Create the examples list of dicts
examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]

example_prompt = PromptTemplate.from_template(
    "Question: {question}\nAnswer: {answer}\n"
)
example_format = "\n".join([example_prompt.format(**ex) for ex in examples])

# Create the few-shot prompt template
few_shot_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are an expert chatbot that answers questions about a user named Jack, "
        "who is a DataCamp user. Use the following examples to answer the question.\n\n"
        "{examples}\n"
        "Question: {question}\nAnswer:"
    ),
    partial_variables={"examples": example_format}
)

def get_response(prompt):
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= [{"role": "user", "content": prompt}], temperature=0)
  
  return response.choices[0].message.content

# Define the user question
user_question = "What is Jack's most recent course on DataCamp?"
# Format the few-shot prompt with the user question
formatted_prompt = few_shot_prompt.format(question=user_question)
# Get the response from the model
response = get_response(formatted_prompt)
print(response)