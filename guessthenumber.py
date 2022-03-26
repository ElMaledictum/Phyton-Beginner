from random import *

to_guess = randint(1, 20)
print ("I'm thinking of a number from (1 to 20): ")
counter = 0
guess_input = 0
while guess_input != to_guess and counter < 6:
    guess_input = int(input('Take a guess: '))
    
    if guess_input < to_guess:
        print (' Your guess is too low! Try again.')
        counter += 1
        continue

    elif guess_input > to_guess:
        print ('Your guess is too high! Try again.')
        counter += 1
        continue

    else:
        counter += 1
        print (f'Good job! You guessed my number in {counter} guesses!')
        break

else: 
    print (f'Nope. The secret number is {to_guess}.' )

