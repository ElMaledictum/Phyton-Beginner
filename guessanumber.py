import random

true_number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess != true_number:
            print("You did not guess correctly! Try again.")
            continue

        else:
            print(f"You guessed it! The number was {true_number}")
            break

    except ValueError:
        print("Please enter a NUMBER!")
        continue
