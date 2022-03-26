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

def random_hand(num):
    """Return a list of two card numbers"""
    numbers = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "J": 10,
        "Q": 10,
        "K": 10,
    }
    num_list = []
    for key in numbers:
        num_list.append(key)
    hand = []
    for c in range(num):
        hand.append(random.choice(num_list))
    return hand #outputs a list

def add_card_to_hand(card_list,n_cards_to_add):
    for x in range(n_cards_to_add):
        card_list.extend(random_hand(1))
    return card_list

def card_sum(card_list):
    numbers = {
        "1": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "J": 10,
        "Q": 10,
        "K": 10,
    }
    sum = 0
    for items in card_list:
        sum = sum + numbers.get(items)
    if sum == 21:
        return 0
    if "1" in card_list and sum>21:
        return sum-10
    return sum

def card_display(card_list):
    """Returns card plus suit"""
    suits = ["H", "S", "D", "C"]
    string = []
    s = random.choice(suits)
    for item in card_list:
        string.append(item + s) 
    return ",".join(string)

def game_decision (user_sum, comp_sum):
    if user_sum> 21:
        return ("You lose!")
    elif user_sum == 0:
        return ("Blackjack! You win!")
    elif comp_sum == 0:
        return "Computer has Blackjack! You lose!"
    elif user_sum > comp_sum:
        return ("You win!")
    elif user_sum < comp_sum:
        return ("You lose!")
    elif user_sum == comp_sum:
        return ("It's a draw.")

def blackjack():
    os.system("cls")
    print (logo())
    user_hand = random_hand(2)
    computer_hand = random_hand(2)
    # user_score = 0
    # comp_score = 0

    print (f"Your cards: {card_display(user_hand)} ({card_sum(user_hand)})" )
    print (f"Computer's first card: {card_display(computer_hand[0])} ({card_sum(computer_hand[0])})" )
    x = 0
    while True:
        to_add_card = input("Get another card? ('y'/'n'): ")
        print ()
        if to_add_card == 'y':
            add_card_to_hand(user_hand, 1)
            if card_sum(user_hand) > 21:
                print (f"Your final hand: {card_display(user_hand)} ({card_sum(user_hand)})")
                print (f"Computer's final hand: {card_display(computer_hand)} ({card_sum(computer_hand)})")
                print ("You lose!")
                # comp_score += 1
                break
            x+= 1
            print (f"Your cards: {card_display(user_hand)} ({card_sum(user_hand)})")
            print (f"Computer's cards: {card_display(computer_hand[:x])} ({card_sum(computer_hand[:x])})" )
            continue

        if to_add_card == 'n':
            if card_sum(computer_hand) < 17:
                add_card_to_hand(computer_hand, 1)
                if card_sum(computer_hand) > 21:
                    print (f"Your final hand: {card_display(user_hand)} ({card_sum(user_hand)})")
                    print (f"Computer's final hand: {card_display(computer_hand)} ({card_sum(computer_hand)})")
                    print ("You win!")
                    # user_score += 1
                    break

            print (f"Your final hand: {card_display(user_hand)} ({card_sum(user_hand)})")
            print (f"Computer's final hand: {card_display(computer_hand)} ({card_sum(computer_hand)})")
            print (game_decision(card_sum(user_hand), card_sum(computer_hand))) #Tells if you win or lose or draw
            break


blackjack()        