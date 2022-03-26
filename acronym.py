string = input("Enter a string: ").upper()

s_list = string.split()

print("Acronym: ", end="")
for x in s_list:
    print(x[0], end="")
