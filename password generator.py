import random
import string

def generate_password():
    print("--- Password Generator ---")
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for i in range(length))
        
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the length.")

generate_password()