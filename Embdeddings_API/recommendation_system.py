from func_create_embeddings import create_embeddings, products
from enriched_embeddings import create_product_text, find_n_closest

last_product = products[-1]

# Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
product_embeddings = create_embeddings(product_texts)

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings, n=3)

for hit in hits:
  product = products[hit['index']]
  print(product['title'])