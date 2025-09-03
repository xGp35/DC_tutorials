from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

ticket = """
Subject: Urgent - Login Error
Hi Support Team,
I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.
Please investigate and assist promptly.
Thanks,
John.
"""

# Craft a prompt to classify the ticket
prompt = f"""Classify the ticket provided within triple backticks. 
The ticket has to be classified in to one of the below 3 categories
- technical issue
- billing inquiry
- product feedback
Don't put anything else in the response.  ```{ticket}```"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)
