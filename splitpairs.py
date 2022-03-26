
a = 'abcdefg'

new = []
len_two = len(a) % 2
a = a + '_'*len_two
for i in range(0,len(a),2):
    list_str = a[i:i+2]
    new.append(list_str)
print (new)