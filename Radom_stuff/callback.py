import time

def fetch_data(callback):
    print("⏳ Fetching data...")
    time.sleep(2)  # Simulating a delay
    callback("📦 Data received!")

def process_data(data):
    print(f"✅ Processing: {data}")

fetch_data(process_data)

# From this it appears that the callback function is just a name given to a fucntion that is called within another function.
# There is no special function called callback. Neither does it behave differently to other funtions.
# It is just another random function that is called inside another function. 
# Whenever a funcion is called inside another function, it is called as callback function.

# Wait.... ⏸️ ChatGPT says that what I said is not fully accurate.
# A callback function is a function passed as an argument to another function. So, in our example I see that 🎃process_data function is passed as an argument to the 🎃fetch_data function.
# So Process_data is the callback function.
# So A callback function is simply a function that is passed as an argument to another function. 
