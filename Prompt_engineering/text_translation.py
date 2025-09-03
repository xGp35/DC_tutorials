from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

marketing_message = """Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality.
Sure! Here is the translation of the provided text into French, Spanish, and Japanese:
"""


# Craft a prompt that translates
prompt = f"Translate the text delmiited by triple backticks to French, Spanish and Japanese```{marketing_message}```"
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)


sample_email = """
Subject: Check out our latest products!
    Dear Customer,    
    We are excited to introduce our latest product line that includes a wide range of items to suit your needs. Whether you're looking for electronics, home appliances, or fashion accessories, we have it all!
    Hurry and visit our website to explore the fantastic deals and discounts we have for you. Don't miss out on the opportunity to get the best products at unbeatable prices.    
    Thank you for being a valued customer, and we look forward to serving you soon!    
    Best regards,
    The Marketing Team
"""


# Craft a prompt to change the email's tone
prompt = f"Change the tone of the email provide within triple backticks. The tone of the output should be professional, positive, and user-centric```{sample_email}```"

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)


after_transforamtion = """
Subject: Discover Our Exciting New Product Line!
    Dear Valued Customer,    
    We are thrilled to share the launch of our latest product line, thoughtfully designed to meet your diverse needs. From cutting-edge electronics to stylish home appliances and fashionable accessories, we have something for everyone!    We invite you to visit our website and explore the exceptional deals and discounts available just for you. This is a wonderful opportunity to find high-quality products at remarkable prices.
    Thank you for being an integral part of our community. We look forward to continuing to serve you and enhancing your experience with us!    
    Warm regards,  
    The Marketing Team
"""

text =  """
Hey guys, wanna know a cool trick? Here's how u can up your productivity game! First, download this awesome app, it's like the best thing ever! Then, just start using it and u'll see the difference. Its super easy and fun, trust me! So, what are u waiting for? Try it out now!
"""

# Craft a prompt to transform the text
prompt = f"""
Transform the text delimited by triple backticks with the following steps:
Step-1: Proof read it without changing the structure
Step-2: Change the tone to be formal and friendly.
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)