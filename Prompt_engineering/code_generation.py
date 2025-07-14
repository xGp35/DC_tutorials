from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content
function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
Modify the function delimited by triple backticks according to the following
Step 1: Test if the inputs to the function are positive
Step 2: Display appropriate error messages if it is not positive
Step 3: If the inputs are valid, return the area and the perimeter of the rectangle
```{function}```
"""

response = get_response(prompt)
print(response)