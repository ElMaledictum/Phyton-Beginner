
number = '0000'
"""counter = 0
for x in number:
    if int(x) == 0:
        counter += 1
    else:
        break
print (counter)
"""
str_int = str(int(number))

print (len(number) - len(str_int) + (str_int == '0'))

print (len(number))
print (len(str_int))
print (str_int =='0')

