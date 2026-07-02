import random
DIFFICULTY_LEVELS = {"1": ("Easy", 1, 50, 10),
                     "2": ("Medium", 1, 100, 7),
                     "3": ("Hard", 1, 200, 5),}
def choose_difficulty():
    print("\nSelect difficulty:")
    for key, (name, low, high, attempts) in DIFFICULTY_LEVELS.items():
        print(f"{key}. {name} (range {low}-{high}, {attempts} attempts)")
    while True:
        choice = input("Enter choice: ").strip()
        if choice in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[choice]
        print("Invalid choice. Try again.")
def get_guess(low, high):
    while True:
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
            if guess < low or guess > high:
                print(f"Please enter a number within range {low}-{high}.")
                continue
            return guess
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def play_round(low, high, max_attempts):
    secret = random.randint(low, high)
    attempts_used = 0
    while attempts_used < max_attempts:
        guess = get_guess(low, high)
        attempts_used += 1
        remaining = max_attempts - attempts_used
        if guess == secret:
            print(f"\nCorrect! You guessed it in {attempts_used} attempt(s).")
            return True
        elif guess < secret:
            print(f"Too low! ({remaining} attempts left)")
        else:
            print(f"Too high! ({remaining} attempts left)")
    print(f"\nOut of attempts! The number was {secret}.")
    return False
def main():
    print("=" * 35)
    print("      NUMBER GUESSING GAME")
    print("=" * 35)
    score = 0
    rounds_played = 0
    while True:
        name, low, high, max_attempts = choose_difficulty()
        print(f"\n--- {name} Round ---")
        won = play_round(low, high, max_attempts)
        rounds_played += 1
        if won:
            score += 1
        print(f"\nScore: {score}/{rounds_played}")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print(f"\nFinal Score: {score}/{rounds_played}. Thanks for playing!")
            break
if __name__ == "__main__":
    main()