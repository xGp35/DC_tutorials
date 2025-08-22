from openai import OpenAI

client = OpenAI(api_key="sk-5678ijklmnopabcd5678ijklmnopabcd5678ijkl")

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)


# -----------------------------------------------------------------------------
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over the user questions
for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")

    