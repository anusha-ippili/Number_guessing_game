import random
import Logo_art  

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return attempts

def game():
    print(Logo_art.Logo)
    print("I'm thinking of a number between 1 and 50.")
    
    answer = random.randint(1, 50)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = set_difficulty(level)
    guessed_number = 0

    while guessed_number != answer:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        try:
            guessed_number = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts = check_answer(guessed_number, answer, attempts)

        if guessed_number == answer:
            break
        elif attempts == 0:
            print(f"You've run out of guesses. You lose! The correct answer was {answer}.")
            return
        else:
            print("Guess again.")

game()