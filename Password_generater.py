import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter the desired password length (or 0 to exit): "))
        if length == 0:
            print("Exiting the password generator. Goodbye!")
            break
        
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}\n")
    except ValueError:
        print("Please enter a valid number.")
