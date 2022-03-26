
translation = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    0 : 'zero'
}

user_input =input('Enter a number: ')
each_digit = (str(user_input))

print ("Translation: ")
output = ''
for number in each_digit:
    int_number = int (number)
    output = output + (translation.get (int_number) + ' ')

print (output)

