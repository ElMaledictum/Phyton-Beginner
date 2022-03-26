import random
import os

os.system("cls")


def compare(user_num, to_guess):
    # global secret_num
    to_guess = secret_num
    if user_num < to_guess:
        print("Too low")
        return "low"
    elif user_num > to_guess:
        print("Too high")
        return "high"
    else:
        print("You guessed it!")
        print(f"The number was {to_guess}")
        return "correct"


def guessing_proper(tries):
    # global secret_num

    while tries > 0:
        print(f"You have {tries} attempts to guess!")
        guess = int(input("Make a guess: "))
        result = compare(guess, secret_num)
        if result == "correct":
            break
        tries -= 1

    else:
        print ("You lose!") 
        return False

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty ('easy'/'hard'): ").lower()
secret_num = random.randint(1, 100)
print(f"HINT: The number is {secret_num}")

if difficulty == "easy":
    guessing_proper(10)
else:
    guessing_proper(5)
