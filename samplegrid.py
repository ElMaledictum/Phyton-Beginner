
grid = [
    [1,2,3],
    ['a', 'b', 'c'],
    ['x','y','z'],
    [4,5,6]
    ]
for x in range(4):
    for y in range (3):
        if y<3:

            print (grid[x][y],end = ' ')

        else:
            print (grid[x],[y])