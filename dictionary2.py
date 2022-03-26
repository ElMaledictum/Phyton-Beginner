import pprint

message = 'aaaccc'
message1 = 'It was a bright cold day in April, and the clocks were striking thirteen.'
counter = {}

for letter in message:
    counter.setdefault(letter, 0)
    counter[letter] = counter[letter] +1

print(len(counter))

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope']
loots = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#def addtoInventory (current_items, added_items):

    