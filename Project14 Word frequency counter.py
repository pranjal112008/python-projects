def word_frequency(text: str) -> dict:
    words = text.lower().split()
    frequency = {}
    for word in words:
        cleaned = ''.join(char for char in word if char.isalnum())
        if not cleaned:
            continue
        frequency[cleaned] = frequency.get(cleaned, 0) + 1
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
