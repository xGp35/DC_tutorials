from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  # loads .env into environment variables

or_token = os.getenv("OPEN_ROUTER_KEY")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=or_token,
)

llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)


completion = client.chat.completions.create(
  model="qwen/qwen3-4b:free",
  max_tokens= 400,
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print("Sending query to OpenRouter-powered OpenAI client...")
print(completion.choices[0].message.content)