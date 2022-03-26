from random import *
from sys import *

wins = 0
losses = 0
ties = 0

print ('ROCK, PAPER, SCISSORS')

while True:
    print (f' {wins} Wins, {losses}, Losses, {ties} Ties \n')
    move = (input('Enter your move: (R)ock, (P)aper, (S)cissors, or (Q)uit: ')).lower()
    
    while True:
        if move == 'q':
            exit ()

        elif move == 'r' or move == 'p' or move == 's':
            break
    
    if move == 'r':
        print ('ROCK versus .... ')

    elif move == 'p':
        print ('PAPER versus .... ')
    
    elif move == 's':
        print ('SCISSORS versus .... ')
    
    opponent = randint (1, 3)

    if opponent == 1:
        opponent_move = 'r'
        print ('ROCK \n')
    
    elif opponent == 2:
        opponent_move = 'p'
        print ('PAPER \n')\

    elif opponent == 3:
        opponent_move = 's'
        print ('SCISSORS \n')

    
    if move == opponent_move:
        print ("It's a tie!")
        ties += 1

    elif move == 'r' and opponent_move == 'p':
        print ('You lose')
        losses += 1

    elif move == 'r' and opponent_move == 's':
        print ('You win!')
        wins += 1

    elif move == 'p' and opponent_move == 's':
        print ('You lose')
        losses += 1

    elif move == 'p' and opponent_move == 'r':
        print ('You win!')
        wins += 1

    elif move == 's' and opponent_move == 'r':
        print ('You lose')
        losses += 1

    elif move == 's' and opponent_move == 'p':
        print ('You win!')
        wins += 1

    #print (f' {wins} Wins, {losses}, Losses, {ties} Ties \n')

