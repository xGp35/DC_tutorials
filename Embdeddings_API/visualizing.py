import multiple_inputs
import matplotlib.pyplot as plt
import numpy as np

# Create categories and embeddings lists using list comprehensions
categories = [product["category"] for product in products]
embeddings = [product["embedding"] for product in products]

# Reduce the number of embeddings dimensions to two using t-SNE
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))