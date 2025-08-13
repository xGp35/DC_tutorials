from chromaDB_intro import client, OpenAIEmbeddingFunction

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

reference_texts = ["children's story about a car", "lions"]

# Query two results using reference_texts
result = collection.query(
  query_texts = reference_texts,
  n_results = 3,
  # Filter for titles with a G rating released before 2019
  where={
    "$and": [
        {"rating": 
        	{"$eq": 'G'}
        },
        {"release_year": 
         	{"$lt" : 2019}
        }
    ]
  }
)

print(result['documents'])