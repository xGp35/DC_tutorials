import requests
from langchain_core.prompts import PromptTemplate
import logging
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}",
    "Content-Type": "application/json"
}

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
def get_response(prompt, max_retries=3):
    """Query Hugging Face's hosted API with retry logic"""
    for attempt in range(max_retries):
        try:
            payload = {"inputs": prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 401:
                logger.error("Authentication failed. Please check your Hugging Face API token")
                return "Error: Authentication failed"
                
            if response.status_code == 429:
                wait_time = 2 ** attempt  # Exponential backoff
                logger.warning(f"Rate limit hit, waiting {wait_time} seconds...")
                time.sleep(wait_time)
                continue
                
            response.raise_for_status()
            
            result = response.json()
            
            if isinstance(result, list):
                return result[0] if isinstance(result[0], str) else result[0].get('generated_text', 'No response generated')
            elif isinstance(result, dict):
                return result.get('generated_text', 'No response generated')
            else:
                return str(result)
                
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                logger.error(f"Failed after {max_retries} attempts: {str(e)}")
                return f"Error: {str(e)}"
            time.sleep(2 ** attempt)
            continue

# Define the user question
user_question = "What is Jack's most recent course on DataCamp?"
formatted_prompt = few_shot_prompt.format(question=user_question)

# Get the response
try:
    response = get_response(formatted_prompt)
    print(f"Response: {response}")
except Exception as e:
    logger.error(f"Error getting response: {str(e)}")