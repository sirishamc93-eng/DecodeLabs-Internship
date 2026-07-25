import secrets
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

length = int(input("Enter password length: "))

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
characters = letters + digits + symbols

# Ensure password has at least one of each type
password = [
    secrets.choice(letters),
    secrets.choice(digits),
    secrets.choice(symbols)
]

# Fill the rest randomly
password += [secrets.choice(characters) for _ in range(length - 3)]

# Shuffle to avoid predictable placement
secrets.SystemRandom().shuffle(password)

print("\nGenerated Password:")
print("".join(password))
