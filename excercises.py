
entered_number = 6

for count in range (entered_number+1):
    output = ''
    for x_count in range(count):
        output = output + '0'
        
    print (output)

for count in range (entered_number-1, 0, -1):
    output = ''
    for x_count in range (count):
        output = output + '0'
    print (output)