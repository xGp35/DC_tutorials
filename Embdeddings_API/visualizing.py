import multiple_inputs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

products = multiple_inputs.products

# Create categories and embeddings lists using list comprehensions
categories = [product["category"] for product in products]
embeddings = [product["embedding"] for product in products]

# Reduce the number of embeddings dimensions to two using t-SNE
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Create a scatter plot from embeddings_2d
plt.scatter(embeddings_2d[:,0], embeddings_2d[:,1])

for i, category in enumerate(categories):
    plt.annotate(category, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.show()