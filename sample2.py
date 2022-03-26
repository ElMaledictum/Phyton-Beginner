x = [1,2,3,4,5,6,7]
y = ['a','b','c','d','e','f','g','h','i']
combined = {}

for key in x:
    for value in y:
        combined[key] = value
        y.remove(value)
print (combined)

