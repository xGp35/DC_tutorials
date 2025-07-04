from openai import OpenAI

client = OpenAI(api_key="ENTER YOUR API KEY HERE")
# The client configures the environment for communicating with the API.

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role": "user", "content": "What is backpropagation?"}],
    max_completion_tokens = 100
)


# client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# response = client.chat.completions.create(
#   # Specify the model
#   model="gpt-4o-mini",
#   messages=[
#     # Assign the correct role
#     {"role": "user", 
#      "content": "Announce my new AI Engineer role on LinkedIn."}]
# )

print(response.choices[0].message.content)