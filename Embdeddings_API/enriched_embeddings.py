from func_create_embeddings import create_embeddings, products
import numpy as np
from scipy.spatial import distance

# Define a function to combine the relevant features into a single string
def create_product_text(product):
  return f"""Title: {product["title"]}
Description: {product["short_description"]}
Category: {product["category"]}
Features: {'; '.join(product["features"])}"""

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = create_embeddings(product_texts)

def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    # Calculate the cosine distance between the query vector and embedding
    dist = distance.cosine(query_vector, embedding)
    # Append the distance and index to distances
    distances.append({"distance": dist, "index": index})
  # Sort distances by the distance key
  distances_sorted = sorted(distances, key=lambda x: x['distance'])
  # Return the first n elements in distances_sorted
  return distances_sorted[0:n]


# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0]

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, n=5)

print(f'Search results for "{query_text}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit["index"]]
  print(product["title"])
