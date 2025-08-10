# Tiktoken is a library by OpenAI that calculates - How much tokens will be created out of a given input dataset.

import csv, os, tiktoken

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

# Load the encoder for the OpenAI text-embedding-3-small model
enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(text)) for text in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', cost_per_1k_tokens*total_tokens/1000)
