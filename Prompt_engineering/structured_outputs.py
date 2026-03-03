from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Create a prompt that generates the table
prompt = "I am Science fiction lover. Give me a table of 10 books that I should read with columns for Title, Author and Year "

# Get the response
response = get_response(prompt)
print(response)


# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Determine the language of the text and generate a suitable title for the the text excerpt"

# Create the output format
output_format = """Use the following format for the output:
- Text: <Given input text>
- Language: <Language of the given text>
- Title: <Generated title>
"""

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape. Birds were chirping happily, and a gentle breeze rustled the leaves of the trees. It was a perfect evening for a leisurely stroll in the park"

# Create the final prompt
prompt = instructions + output_format+ f"```{text}```"
response = get_response(prompt)
print(response)