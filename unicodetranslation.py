user_word = input("Enter a string to hide: ")
code_numbers = ""
for each_char in user_word:
    ord_of_letter = str(ord(each_char) - 23)
    if each_char == " ":
        ord_of_letter = str(ord(" "))
    code_numbers += ord_of_letter

print(f"Unicode: {code_numbers}")

code_letters = ""
for num in range(0, len(code_numbers) - 1, 2):
    c = int((code_numbers[num]) + (code_numbers[num + 1]))
    if c == 32:
        code_letters += chr(32)

    else:
        code_letters += chr(c + 23)

print(f"Original message: {code_letters}")
