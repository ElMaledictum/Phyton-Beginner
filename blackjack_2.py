import random
import os

def logo():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """
    return logo

def all_cards():
    suit = ["S", "D", "C", "H"]
    numbers = ['00A', '002', '003', '004', '005', '006', '007', '008', '009', '010', '00J', '00Q','00K']
    card_list = []
    for s in suit:
        for n in numbers:
            card_list.append(n+s)
    return card_list
deck = all_cards()

def card_sum(card_list):
    values = {
        "00A": 11,
        "002": 2,
        "003": 3,
        "004": 4,
        "005": 5,
        "006": 6,
        "007": 7,
        "008": 8,
        "009": 9,
        "010": 10,
        "00J": 10,
        "00Q": 10,
        "00K": 10,
    }
    sum = 0
    for i in range(len(card_list)):
        value = values[card_list[i][:3]]    
        sum += value
        if card_list[i][:3] == '00A' and sum> 21:
            sum -= 10
    return sum

def add_card():
    """Adds card to user and computer hand. Removes from deck.
    Return a string of 00XXY"""
    global deck
    card = []
    c = random.choice(deck)
    deck.remove(c)
    card.append(c)
    return card

def card(card_list):
    """Receives list of card then remove 00"""
    converted = []
    for i in range(len(card_list)):
        x = card_list[i].strip("0")
        converted.append(x)
    return converted

def display(string, u_cards, c_cards):
    if string == "l":
        return (f"Your final hand: {', '.join(card(u_cards))} ({card_sum(u_cards)})\n\
Computer's final hand: {', '.join(card(c_cards))} ({card_sum(c_cards)})\n\
You lose!")

    elif string == 'c':
        comp_c_string = ', '.join(card(c_cards))     
        return (f"Your hand: {', '.join(card(u_cards))} ({card_sum(u_cards)})\n\
Computer's first card: {comp_c_string[:3]}\n")

    elif string == "w":
        return (f"Your final hand: {', '.join(card(u_cards))} ({card_sum(u_cards)})\n\
Computer's final hand: {', '.join(card(c_cards))} ({card_sum(c_cards)})\n\
You win!")
    elif string == "d":
        return (f"Your final hand: {', '.join(card(u_cards))} ({card_sum(u_cards)})\n\
Computer's final hand: {', '.join(card(c_cards))} ({card_sum(c_cards)})\n\
It's a draw!")

def game_proper():
    os.system('cls')
    print (logo())
    u_score = 0
    c_score = 0
    user_cards = []
    computer_cards = []
    for x in range (2):
        user_cards.extend(add_card())
        computer_cards.extend(add_card())

    user_c_string = ', '.join(card(user_cards))
    comp_c_string = ', '.join(card(computer_cards))     

    print (f"Your cards: {user_c_string} ({card_sum(user_cards)})")
    print (f"Computer's first card: {comp_c_string[:3]} ")


    while True:  
        answer = input("Get another card? ('y'/'n'): ").lower()
        print ()
        if answer == 'y':
            user_cards.extend(add_card())
            if card_sum(user_cards)> 21:
                print (display("l", user_cards, computer_cards)) #display you lose
                c_score += 1
                break
            print (display("c", user_cards, computer_cards))
            continue
        elif answer =='n':
            while card_sum(computer_cards) < 17:
                computer_cards.extend(add_card()) 
                   
        
        if card_sum(user_cards)> 21:
            print (display("l", user_cards, computer_cards)) #display you lose
            c_score += 1
            break

        elif card_sum(computer_cards) > 21:
            print (display("w", user_cards, computer_cards)) #display you win
            u_score += 1
            break
        
        elif card_sum(user_cards)> card_sum(computer_cards):
            print (display("w", user_cards, computer_cards)) #display you win
            u_score += 1
            break
            
        elif card_sum(user_cards)< card_sum(computer_cards):
            print (display("l", user_cards, computer_cards)) #display you lose
            c_score += 1
            break
            
        elif card_sum(user_cards)== card_sum(computer_cards):
            print (display("d", user_cards, computer_cards)) #display you lose
            break

    print (f"You: {u_score}  ---------- Computer: {c_score}")

        

while input("Do you want to play blackjack? (y/n)") == 'y':
    game_proper()
print (len(deck))
