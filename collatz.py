def collatz(number):

    if (number % 2) == 0:
        number = number // 2
        print(number)
        return number

    elif (number % 2) == 1:
        result = 3 * number + 1
        print(result)
        return result


try:
    user_input = int(input("Enter a number: "))
    while user_input != 1:
        # print (user_input, end = ' ')
        user_input = collatz(user_input)

except ValueError:
    print("Invalid input!")
