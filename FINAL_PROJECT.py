import random
import os

class Question:
    def __init__(self, prompt, answers, correct):
        self.prompt = prompt
        self.answers = answers
        self.correct = correct

geography_questions = [
    Question(
        "What is the capital of France?",
        ["Paris", "London", "Berlin", "Madrid"],
        0
    ),
    Question(
        "Which river is the longest in South America?",
        ["Orinoco River", "Rio Grande", "Amazon River", "Magdalena River"],
        2
    ),
    Question(
        "What is the largest desert in the world?",
        ["Atacama Desert", "Gobi Desert", "Mojave Desert", "Sahara Desert"],
        3
    ),
    Question(
        "Which mountain range runs along the border between France and Spain?",
        ["Caucasus", "Alps", "Carpathian Mountains", "Pyrenees"],
        3
    ),
    Question(
        "What is the world's largest waterfall, by volume of water?",
        ["Victoria Falls", "Angel Falls", "Iguazu Falls", "Niagara Falls"],
        0
    )
]

word_lists = {
    "fruits": ["apple", "mango", "grape", "peach", "berry"],
    "animals": ["tiger", "zebra", "whale", "eagle", "sheep"],
    "countries": ["chile", "japan", "italy", "egypt", "india"]
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("\n-----Hello Welcome to our game!-----")
    print("\nPICK TO START")
    print("1. QUIZ")
    print("2. WORDLE")
    print("3. EXIT\n")

def run_quiz():
    score = 0
    total_questions = len(geography_questions)
    
    print("\n=== Geography Quiz ===\n")
    for question in geography_questions:
        print(question.prompt)
        
        for i, answer in enumerate(question.answers):
            print(f"{chr(65 + i)}) {answer}")
        user_answer = input("Enter your choice (A-E): ").upper()
        if ord(user_answer[0]) - 65 == question.correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question.answers[question.correct]}.\n")
    
    print("\nQuiz completed!")
    print(f"Your final score is {score}/{total_questions}")
    input("\nPress Enter to continue...")

def choose_category():
    print("Choose a category:")
    for category in word_lists.keys():
        print(f"- {category}")
    while True:
        category = input("Enter category: ").lower()
        if category in word_lists:
            return category
        else:
            print("Invalid category. Please choose again.")

def get_random_word(category):
    return random.choice(word_lists[category])

def get_feedback(guess, secret_word):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")  
        elif guess[i] in secret_word:
            feedback.append("🟨")  
        else:
            feedback.append("⬜")  
    return ''.join(feedback)

def play_wordle():
    category = choose_category()
    secret_word = get_random_word(category)
    attempts = 5
    
    print(f"\nGuess the 5-letter word from the category '{category}'!")
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Enter your guess: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess == secret_word:
            print("Congratulations! You've guessed the word correctly!")
            break
        feedback = get_feedback(guess, secret_word)
        print(f"Feedback: {feedback}")
        attempts -= 1
        if attempts == 0:
            print(f"Sorry, you've run out of attempts! The word was '{secret_word}'")
    input("\nPress Enter to continue...")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            run_quiz()
        elif choice == '2':
            play_wordle()
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()