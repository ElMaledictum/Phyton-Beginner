
orig_word = input('Enter a word: ')



for index in range (len(orig_word),0, -1):
    print (orig_word[index-1], end ="")

print ("\n")