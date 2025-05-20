import secrets
import string

def generate_password(length, use_special_chars=True):
    if length < 6:
        return "Password length must be at least 6 for security."

    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Ensure at least one of each required type
    required_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(digits),
        secrets.choice(special_chars) if use_special_chars else secrets.choice(letters)
    ]

    # Fill the rest randomly
    all_chars = letters + digits + special_chars
    remaining_chars = [secrets.choice(all_chars) for _ in range(length - len(required_chars))]

    # Shuffle and join to form final password
    password_list = required_chars + remaining_chars
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

# User Input
password_length = int(input("Enter the desired password length: "))
use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

# Generate Password
generated_password = generate_password(password_length, use_special)

# Display
print("Generated Password:", generated_password)