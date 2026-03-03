from func_create_embeddings import create_embeddings, products
from enriched_embeddings import create_product_text, find_n_closest

# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(article) for article in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = list(filter(lambda product: product not in user_history, products))

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products]
product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
  product = products_filtered[hit['index']]
  print(product['title'])