def word_frequency(text: str) -> dict:
    words = text.lower().split()
    cleaned_words = [''.join(char for char in word if char.isalnum()) for word in words]
    cleaned_words = [word for word in cleaned_words if word]
    unique_words = {word for word in cleaned_words}
    frequency = {word: cleaned_words.count(word) for word in unique_words}
    return frequency
def print_frequency(frequency: dict):
    print("\nWord Frequency:")
    print("-" * 25)
    for word, count in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{word:<15} {count}")
if __name__ == "__main__":
    text = input("Enter a sentence or paragraph: ").strip()
    if not text:
        print("Please enter some text!")
    else:
        result = word_frequency(text)
        print_frequency(result)
        most_common = max(result, key=result.get)
        print(f"\nMost common word: '{most_common}' ({result[most_common]} times)")
