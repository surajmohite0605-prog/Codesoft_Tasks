import random
import string

# User input
length = int(input("Enter password length: "))

# Characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display password
print("Generated Password:", password)