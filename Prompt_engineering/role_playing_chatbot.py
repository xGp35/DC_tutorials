from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")


def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Craft the system_prompt using the role-playing approach
system_prompt = """You are an expert chatbot that recommends textbooks to users. Your role is to act as a learning advisor who can interpret learner queries and provide relevant information as mentioned in the following steps

Step 1: Receive quries from learners about their background, experience and goals
Step 2: Recommend a learning path of textbooks, including both beginner-level and advanced options.
"""

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)


base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "Ask the user about their background, experience, and goals, whenever any of these is not provided in the prompt."

# Define response guidelines
response_guidelines = "Don't recommend more than three textbooks"

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)