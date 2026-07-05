import random
import string
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    guaranteed = []
    if use_upper:
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_lower:
        guaranteed.append(random.choice(string.ascii_lowercase))
    if use_digits:
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        guaranteed.append(random.choice(string.punctuation))
    if length < len(guaranteed):
        raise ValueError(f"Length must be at least {len(guaranteed)} for the selected options.")
    remaining_length = length - len(guaranteed)
    password_chars = guaranteed + [random.choice(character_pool) for _ in range(remaining_length)]
    random.shuffle(password_chars)
    return "".join(password_chars)
def rate_strength(length, use_upper, use_lower, use_digits, use_symbols):
    variety = sum([use_upper, use_lower, use_digits, use_symbols])
    if length >= 16 and variety >= 3:
        return "Very Strong"
    elif length >= 12 and variety >= 3:
        return "Strong"
    elif length >= 8 and variety >= 2:
        return "Moderate"
    else:
        return "Weak"
def get_yes_no(prompt, default_yes=True):
    suffix = " (Y/n): " if default_yes else " (y/N): "
    answer = input(prompt + suffix).strip().lower()
    if answer == "":
        return default_yes
    return answer == "y"
def get_length():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Length must be at least 4.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def main():
    print("=" * 35)
    print("       PASSWORD GENERATOR")
    print("=" * 35)
    while True:
        length = get_length()
        use_upper = get_yes_no("Include uppercase letters?")
        use_lower = get_yes_no("Include lowercase letters?")
        use_digits = get_yes_no("Include digits?")
        use_symbols = get_yes_no("Include symbols?", default_yes=False)
        try:
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            strength = rate_strength(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"\nGenerated Password: {password}")
            print(f"Strength: {strength}")
        except ValueError as e:
            print(f"Error: {e}")
        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()