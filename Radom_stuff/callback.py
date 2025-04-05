import time

def fetch_data(callback):
    print("⏳ Fetching data...")
    time.sleep(2)  # Simulating a delay
    callback("📦 Data received!")

def process_data(data):
    print(f"✅ Processing: {data}")

fetch_data(process_data)
