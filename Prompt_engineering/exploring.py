from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT")
print(response)

prompt = "Write a one-sentence bedtime story about a unicorn."
response = get_response(prompt)

prompt2 = "Write a poem about ChatGPT that is written in basic English that a child can understand"
response2 = get_response(prompt2)

story = "In a distant galaxy, there was a brave space explorer named Alex. Alex had spent years traveling through the cosmos, discovering new planets and meeting alien species. One fateful day, while exploring an uncharted asteroid belt, Alex stumbled upon a peculiar object that would change the course of their interstellar journey forever..."

prompt3 = f"Complete the story delimited by triple backticks ```{story}```"

prompt4 = f"Complete the story delimited by triple backticks with only two paragraphs in the style of Shakespeare```{story}``` "


