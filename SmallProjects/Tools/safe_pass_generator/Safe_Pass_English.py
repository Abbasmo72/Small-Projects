import secrets
import string

def generate_strong_password(length=12):
    """Generate a strong random password of specified length."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    # Character set: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Test the function
password = generate_strong_password(16)
print("Generated random password:", password)
