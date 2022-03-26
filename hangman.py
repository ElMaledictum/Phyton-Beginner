from ctypes import cdll
import random
import time
import hangmangraphics
import os


def all_filled(blank_list):
    if "_" in blank_list:
        return False
    else:  # puno na ng letters
        return True


def create_word():
    import hangmandwordlist

    word_list = hangmandwordlist.word_list
    random_word = random.choice(word_list)
    return random_word


def hang_graphic(int):
    stages = [
        """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    """,
        """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    """,
        """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    """,
        """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
        """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
        """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
        """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    ]
    return stages[int]


print(hangmangraphics.logo)
chosen_word = create_word()
# print(chosen_word)
blanks = []
for x in range(len(chosen_word)):
    blanks.append("_")

lives = 6
print(" ".join(blanks))

while True:
    time.sleep(0.1)
    guessed_letter = input("Guess a letter in the word: ").lower()

    os.system("cls")

    if guessed_letter not in chosen_word:
        lives -= 1
        time.sleep(0.1)
        print(f"No letter {guessed_letter}.")
        print(hang_graphic(lives))

        if lives == 0:
            time.sleep(0.2)
            print("You lose!")
            print(f"The word is {chosen_word}.")
            break
    else:
        time.sleep(0.1)
        print("Good!")
        print(hang_graphic(lives))

    if guessed_letter in blanks:
        print(f"You've already guessed {guessed_letter}.\nYou lose a life!")
        lives -= 1
        print(hang_graphic(lives))

        if lives == 0:
            time.sleep(0.2)
            print("You lose!")
            print(f"The word is {chosen_word}.")
            break

    for index, each_char in enumerate(chosen_word):
        if each_char == guessed_letter:
            blanks[index] = guessed_letter

    if all_filled(blanks) and lives > 0:
        time.sleep(0.2)
        print("You won! Congratulations!")
        break

    print(" ".join(blanks))


