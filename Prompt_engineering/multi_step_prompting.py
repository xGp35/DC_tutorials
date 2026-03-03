from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Create a prompt detailing steps to plan the trip
prompt = """Create a plan for a beach vacation which:
1. Should include four potential locations.
2. Each location should have some accommodation options, some activities and evaluation of the pros and cons.
"""

response = get_response(prompt)
print(response)

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""You are given some python code delimited by triple backticks. 
```{code}```
Assess the function in the delimited code according to the following criteria - correct syntax, receiving two inputs, and returning one output.
"""

response = get_response(prompt)
print(response)