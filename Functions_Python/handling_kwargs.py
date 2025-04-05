def greet(**kwargs):
    name = kwargs.get("name", "Guest")  # Default to "Guest" if missing
    greeting = kwargs.get("greeting", "Hello")  # Default greeting
    return f"{greeting}, {name}!"

print(greet(name="Alice", greeting="Hey"))  # ✅ "Hey, Alice!"
print(greet(name="Bob"))                    # ✅ "Hello, Bob!"
print(greet())                               # ✅ "Hello, Guest!"
