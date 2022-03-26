#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print (len(numbers))
print("Welcome to the PyPassword Generator!")
number_of_letters= int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pword = ""
for x in range(0, number_of_letters):
    random_char = random.randint(0,51)
    pword += letters[random_char]
# print (pword)
for x in range(0, number_of_symbols):
    random_char = random.randint(0,8)
    pword += symbols[random_char]
# print (pword)
for x in range(0, number_of_numbers):
    random_char = random.randint(0,9)
    pword += numbers[random_char]
p_list = list(pword)
random.shuffle(p_list)
print (f"Here is your password: {''.join(p_list)}")

