import random
CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock"    : "scissors",
         "paper"   : "rock",
         "scissors": "paper",}
def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors (r/p/s): ").strip().lower()
        mapping = {"r": "rock", "p": "paper", "s": "scissors"}
        if choice in mapping:
            return mapping[choice]
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please enter rock, paper, scissors (or r/p/s).")
def get_computer_choice(strategy, history):
    """
    strategy:
      - "random": pure random pick
      - "adaptive": tries to counter the player's most frequent choice
    """
    if strategy == "adaptive" and history:
        unique_choices = {choice for choice in history}
        most_common = max(unique_choices, key=history.count)
        counter = {v: k for k, v in BEATS.items()}[most_common]
        return counter
    return random.choice(CHOICES)
def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"
def choose_strategy():
    print("\nChoose computer difficulty:")
    print("1. Random (fair)")
    print("2. Adaptive (learns your patterns - harder)")
    choice = input("Enter choice: ").strip()
    return "adaptive" if choice == "2" else "random"
def main():
    print("=" * 35)
    print("     ROCK PAPER SCISSORS")
    print("=" * 35)
    strategy = choose_strategy()
    player_history = []
    player_score = 0
    computer_score = 0
    ties = 0
    round_num = 0
    while True:
        round_num += 1
        player_choice = get_player_choice()
        computer_choice = get_computer_choice(strategy, player_history)
        player_history.append(player_choice)
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = decide_winner(player_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"\nScore -> You: {player_score} | Computer: {computer_score} | Ties: {ties}")
        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            break
    print("\n" + "=" * 35)
    print("           FINAL RESULTS")
    print("=" * 35)
    print(f"Rounds played : {round_num}")
    print(f"You           : {player_score}")
    print(f"Computer      : {computer_score}")
    print(f"Ties          : {ties}")
    if player_score > computer_score:
        print("\nOverall winner: YOU! 🎉")
    elif computer_score > player_score:
        print("\nOverall winner: Computer")
    else:
        print("\nOverall result: Tie")
if __name__ == "__main__":
    main()
