from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

report = """In recent years, the intersection of artificial intelligence (AI) and data privacy has become a focal point of discussion among technologists, policymakers, and the public. As AI systems increasingly rely on vast amounts of data to learn and make decisions, concerns about how this data is collected, stored, and used have intensified. The potential for AI to enhance efficiency and innovation is tempered by the risks of data breaches, misuse of personal information, and the erosion of privacy rights.
The European Union's General Data Protection Regulation (GDPR) has set a precedent for data privacy legislation, mandating strict guidelines on data handling and user consent. This regulatory framework has prompted organizations worldwide to reassess their data practices and implement measures to ensure compliance. However, the rapid pace of AI development often outstrips the ability of existing laws to keep up, leading to calls for new regulations that specifically address the unique challenges posed by AI technologies.
Moreover, the ethical implications of AI in relation to data privacy cannot be overlooked. Issues such as algorithmic bias, transparency, and accountability are critical as AI systems become more autonomous. The need for ethical AI practices is underscored by the potential for AI to perpetuate existing inequalities if not designed and monitored carefully. As such, the conversation around AI and data privacy is not just about compliance with laws but also about fostering trust and ensuring that AI technologies are developed and deployed in a manner that respects individual privacy rights.
In conclusion, the relationship between AI and data privacy is complex and multifaceted. As AI continues to evolve, so too must our approaches to data privacy. This includes not only adhering to existing regulations but also proactively addressing the ethical implications of AI technologies. The future of AI and data privacy will depend on collaborative efforts between governments, industry leaders, and civil society to create a framework that balances innovation with the protection of personal data. Only through such collaboration can we ensure that AI serves the public good while respecting the fundamental right to privacy."""

# Craft a prompt to summarize the report
prompt = f"""Summarize the text delimited by triple backticks, in maximum five sentences while focusing on AI and data privacy
```{report}```
"""

response = get_response(prompt)

print("Summarized report: \n", response)


product_description = """The Smartphone XYZ-5000 is a device packed with innovative features to enhance the user experience. Its sleek design and vibrant display make it visually appealing, while the powerful octa-core processor ensures smooth performance and multitasking capabilities.
The XYZ-5000 boasts a high-resolution triple-camera system, combining a 48MP primary lens, a 12MP ultra-wide lens, and a 5MP depth sensor, enabling users to capture stunning photos and videos in various shooting scenarios. The device also supports 4K video recording and comes with advanced image stabilization features.
With a generous 128GB of internal storage, expandable up to 512GB via microSD, users can store a vast collection of media files and apps without worrying about running out of space. The smartphone runs on the latest Android OS and offers seamless integration with various Google services.
In terms of security, the XYZ-5000 features a reliable fingerprint sensor and facial recognition technology for quick and secure unlocking. Additionally, it supports NFC for contactless payments and has a dedicated AI-powered virtual assistant to simplify daily tasks.
The device's long-lasting 4000mAh battery ensures all-day usage, and it supports fast charging, providing hours of power with just a few minutes of charging. The XYZ-5000 is also water and dust resistant, giving users peace of mind in various environments.
Overall, the Smartphone XYZ-5000 offers a fantastic combination of style, performance, and advanced features, making it an excellent choice for tech enthusiasts and everyday users alike.
"""



# Craft a prompt to summarize the product description
prompt = f"""Summarize the text delimited by triple backticks in no more than five bullet points. 
```{product_description}```
The delimited text contains product description and the summary you generate should appeal to the user looking at the product.
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)

product_description = """
Product: "Smart Home Security Camera"
- High-tech security camera with night vision and motion detection.
- Easy setup and remote monitoring.
- Two-way audio communication for real-time interaction.
- Mobile app integration for convenient control and alerts.
- Weather-resistant design for both indoor and outdoor use.
- Smart AI algorithms for advanced person and object detection.
- Cloud storage and local backup options for recorded footage.
- Infrared LEDs for clear imaging even in complete darkness.
- Customizable motion zones to focus on specific areas.
- Compatibility with voice assistants for hands-free control.
"""

# Craft a prompt to expand the product's description
prompt = f"""Expand the description delimited by triple backticks to provide a comprehensive overview capturing key information about the product such as unique features, benefits and potential applications in one paragraph```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)

Expanded_description =  """The "Smart Home Security Camera" is a cutting-edge surveillance solution designed to enhance home security with its array of advanced features. Equipped with night vision and motion detection capabilities, this camera ensures comprehensive monitoring around the clock, even in complete darkness, thanks to its infrared LEDs. The easy setup process and mobile app integration allow users to remotely control the camera and receive real-time alerts, making it convenient to keep an eye on their property from anywhere. Its two-way audio communication feature enables real-time interaction, providing an added layer of security and convenience. The weather-resistant design makes it suitable for both indoor and outdoor applications, while smart AI algorithms enhance its functionality by offering advanced person and object detection. Users can customize motion zones to focus on specific areas of interest, ensuring that they only receive alerts for relevant activity. Additionally, the camera supports both cloud storage and local backup options for recorded footage, ensuring that important video evidence is securely stored. With compatibility for voice assistants, this smart camera offers hands-free control, making it an ideal choice for tech-savvy homeowners looking to bolster their security measures effortlessly."""
