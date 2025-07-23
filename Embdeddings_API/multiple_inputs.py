from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_KEY>")

products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    }
]

# Extract a list of product short descriptions from products
product_descriptions = [product["short_description"] for product in products]

# Create embeddings for each product description
response = client.embeddings.create(
    model = "text-embedding-3-small",
    input = product_descriptions
)
response_dict = response.model_dump()

# Extract the embeddings from response_dict and store in products
for i, product in enumerate(response_dict["data"]):
    product['embedding'] = response_dict["data"][i]["embedding"]
    
print(products[0].items())

# Here's the keys and values for the first review, showing the embeddings have been successfully created and stored. Being able to create embeddings for multiple inputs and store the results for later use will enable so many more use cases.

