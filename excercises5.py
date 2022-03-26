"""
How tall is the tree : 5
0000#
   ###
  #####
 #######
#########
    #


"""

height = int(input("Enter height of tree: "))
width = (height * 2) - 1
reset = width
i = 1
p_counter = 1
while i <= height:
    for x in range((width - 1) // 2):
        print(" ", end="")
    width -= 2
    for y in range(p_counter):
        print("#", end="")

    print("")

    p_counter += 2
    i += 1

for x in range((reset - 1) // 2):
    print(" ", end="")

print("#")
