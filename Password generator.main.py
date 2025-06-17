import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    """Generates a random password based on the specified criteria."""
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_special_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print(f"Error: {e}")
