from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_KEY>")

short_description = ""
list_of_descriptions = []

# Define a create_embeddings function
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]

# Embed short_description and print
print(create_embeddings(short_description)[0])
# Used [0] because the function create_embeddings returns a list, and we just need the first element of the list.

# Embed list_of_descriptions and print
print(create_embeddings(list_of_descriptions))