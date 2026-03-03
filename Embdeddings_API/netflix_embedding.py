from chromaDB_intro import client, OpenAIEmbeddingFunction
import os, csv

ids = []
documents = []

# Path of the script itself
script_dir = os.path.dirname(os.path.abspath(__file__))

# Join with CSV filename
csv_path = os.path.join(script_dir, "netflix_titles_1000.csv")

with open(csv_path, encoding="utf-8") as csvfile:
  reader = csv.DictReader(csvfile)
  for i, row in enumerate(reader):
    ids.append(row['show_id'])
    text = f"Title: {row['title']} ({row['type']})\nDescription: {row['description']}\nCategories: {row['listed_in']}"
    documents.append(text)

# Recreate the netflix_titles collection
collection = client.create_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(
    model_name="text-embedding-3-small", 
    api_key="<OPENAI_API_TOKEN>")
)

# Add the documents and IDs to the collection
collection.add(
  ids = ids,
  documents = documents
)

# Print the collection size and first ten items
print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek()}")