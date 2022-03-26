import os


def addition(a, b):
    """Returns sum of two numbers"""
    return a + b


def subtraction(a, b):
    """Returns the differemce of two numbers"""
    return a - b


def multiplication(a, b):
    """Returns product of two numbers"""
    return a * b


def division(a, b):
    """Returns the quotient of two numbers"""
    return a / b


def print_logo():
    """Print the calculator logo"""
    logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
    return logo


print(print_logo())


def calculator_process():
    continue_calc = "n"
    result = 0
    op_dict = {"+": addition, "-": subtraction, "*": multiplication, "/": division}
    while True:
        if continue_calc == "y":
            print(f"The first number will be {result}")
            first_num = result

        elif continue_calc == "n":
            first_num = float(input("What's the first number? "))

        for keys in op_dict:
            print(keys)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number? "))

        result = op_dict[operation](first_num, second_num)
        # result = operate(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        continue_calc = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )
        if continue_calc == "y":
            continue
        elif continue_calc == "n":
            os.system("cls")
            calculator_process()  # recursion of the calculator


calculator_process()
