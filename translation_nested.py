
# vowels -> g
# dog -> dgg
# cat -> cgt

def translator (sample_string):
    translation = ''

    for each_letter in sample_string:
        if each_letter in 'AEIOUaeiou':
            translation += 'g'

        else:
            translation += each_letter

    return (translation)


user_input = input('Enter a word: ')

print (translator(user_input))

print (user_input[0])