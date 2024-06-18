import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

password_length = int(input("Enter the desired length of the password: "))
print(generate_password(password_length))