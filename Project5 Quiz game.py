import random
QUESTIONS = [{"question": "What is the capital of France?",
               "options": ["A. Berlin",
                           "B. Madrid", 
                           "C. Paris", 
                           "D. Rome"],
                "answer": "C",},
             {"question": "Which language is this quiz written in?",
               "options": ["A. Java", 
                           "B. Python", 
                           "C. C++",
                           "D. Ruby"],
                "answer": "B",},
             {"question": "What is 7 x 8?",
              "options": ["A. 54", 
                          "B. 56",
                          "C. 58",
                          "D. 64"],
                "answer": "B",},
             {"question": "Which planet is known as the Red Planet?",
              "options": ["A. Venus",
                          "B. Jupiter",
                          "C. Mars",
                          "D. Saturn"],
                 "answer": "C",},
              {"question": "What does CPU stand for?",
                "options": [ "A. Central Process Unit",
                             "B. Central Processing Unit",
                             "C. Computer Personal Unit",
                             "D. Central Programming Unit",],
                 "answer": "B",},
             {"question": "Which data type is immutable in Python?",
               "options": ["A. List",
                           "B. Dictionary",
                           "C. Set",
                           "D. Tuple"],
                 "answer": "D",},
             { "question": "What is the boiling point of water at sea level (°C)?",
                "options": ["A. 90", 
                            "B. 95", 
                            "C. 100", 
                            "D. 110"],
                 "answer": "C",},]
def ask_question(q, number, total):
    print(f"\nQuestion {number}/{total}: {q['question']}")
    for option in q["options"]:
        print(option)
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        print("Invalid input. Please enter A, B, C, or D.")
def get_num_questions(max_available):
    while True:
        try:
            n = int(input(f"How many questions do you want to play? (1-{max_available}): "))
            if 1 <= n <= max_available:
                return n
            print(f"Please enter a number between 1 and {max_available}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def run_quiz(num_questions):
    pool = QUESTIONS.copy()
    score = 0
    wrong_answers = []
    for i in range(1, num_questions + 1):
        q = random.choice(pool)
        pool.remove(q)  # prevent repeats within this round
        user_answer = ask_question(q, i, num_questions)
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was {q['answer']}.")
            wrong_answers.append((q["question"], q["answer"], user_answer))
    return score, num_questions, wrong_answers
def show_results(score, total, wrong_answers):
    percentage = (score / total) * 100
    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Score: {score}/{total} ({percentage:.1f}%)")
    if percentage == 100:
        print("Perfect score! 🎉")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 40:
        print("Not bad, keep practicing!")
    else:
        print("Keep studying, you'll improve!")
    if wrong_answers:
        print("\nReview your mistakes:")
        for question, correct, given in wrong_answers:
            print(f" - {question}\n   Your answer: {given} | Correct: {correct}")
    print("=" * 40)
def main():
    print("=" * 40)
    print("          QUIZ GAME (RANDOM MODE)")
    print("=" * 40)
    while True:
        num_questions = get_num_questions(len(QUESTIONS))
        score, total, wrong_answers = run_quiz(num_questions)
        show_results(score, total, wrong_answers)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()