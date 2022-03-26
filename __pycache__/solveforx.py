
ex = input('Enter expression: ')

def solve_for_x (expression):
    x_list = expression.split()
    if x_list[1] == '+':
        return (int(x_list[-1]) - int(x_list[2]))
    elif x_list[1] == '-':
        return (int(x_list[-1]) + int(x_list[2]))

print (f'x = {solve_for_x(ex)}')