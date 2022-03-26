string = input("Enter a string: ")
num_to_shift = int(input("Number to shift (1-26): "))

if num_to_shift > 26:
    print("There are only 26 letters in the alphabet!")

trans_string = ""
for char in string:
    if char.isalpha():
        char_code = ord(char)
        char_code += num_to_shift

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            
            if char_code < ord('A'):
                char_code += 26
        
        else:
            if char_code > ord('z'):
                char_code -= 26
            
            if char_code < ord('a'):
                char_code += 26
        
        trans_string += chr(char_code)
    else:
        trans_string += char
print ("Translated: ", trans_string)

def decryption (message,num):
    trans_string = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code -= num

            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                
                if char_code < ord('A'):
                    char_code += 26
            
            else:
                if char_code > ord('z'):
                    char_code -= 26
                
                if char_code < ord('a'):
                    char_code += 26
            
            trans_string += chr(char_code)
        else:
            trans_string += char

    return trans_string

print ("Decrypted: ", decryption(trans_string, num_to_shift))

