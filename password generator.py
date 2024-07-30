import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """
    Generate a random password.

    :param length: Length of the password (default: 12)
    :param use_uppercase: Include uppercase letters (default: True)
    :param use_numbers: Include numbers (default: True)
    :param use_special_chars: Include special characters (default: True)
    :return: Generated password as a string
    """
    # Base characters: lowercase letters
    characters = string.ascii_lowercase
    
    # Add uppercase letters if required
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Add numbers if required
    if use_numbers:
        characters += string.digits
    
    # Add special characters if required
    if use_special_chars:
        characters += string.punctuation
    
    # Ensure at least one character of each type is included if those types are requested
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))
    
    # Fill the remaining length of the password with random choices from the combined set
    while len(password) < length:
        password.append(random.choice(characters))
    
    # Shuffle the result to ensure randomness and return as a string
    random.shuffle(password)
    return ''.join(password)

# Example usage:
print(generate_password(16))