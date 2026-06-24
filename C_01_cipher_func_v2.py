# functions
def int_check(question):
    """Checks users enter an integer."""

    error = "Please enter an integer between 0 and 26."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            if 0 < response < 26:
                return response
        
            else:
                print(error)

        except ValueError:

            print(error)


def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    result = ''

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:1]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def cipher_func(mode):
    '''Encrypts/Decrypts user input'''

    CHAR_RANGE = 26

    result = ''

    if mode == "encrypt":
        text = input("Plain text: ")
        print()
        shift = int_check("Shift amount: ")
        print()

    elif mode == 'decrypt':
        text = input("Cipher Text: ")
        decrypted_messages = ""
        print()
        shift = 25
    
    else:
        return

    while shift > 0:

        for char in text:
            if char.isupper():
                FIRST_CHAR_CODE = 65
                LAST_CHAR_CODE = 90

            if char.islower():
                FIRST_CHAR_CODE = 97
                LAST_CHAR_CODE = 122

            if char.isalpha():
                char_code = ord(char)
                new_char_code = char_code + shift

                if new_char_code > LAST_CHAR_CODE:
                    new_char_code -= CHAR_RANGE
                
                if new_char_code < FIRST_CHAR_CODE:
                    new_char_code += CHAR_RANGE

                new_char = chr(new_char_code)
                result += new_char
            else:
                result += char

        if mode == 'decrypt':
            print(f"Shift {26-shift}: {result}")
            decrypted_messages += result + ', '
            result = ""
            shift -= 1
            
        if mode == 'encrypt':
            print(f"Encrypted Text: {result}\n")
            break


# main


while True:
    
    mode = string_check("Encrypt or Decrypt? ", ['encrypt', 'decrypt', 'xxx'])
    print()

    if mode == 'xxx':
        break

    cipher_func(mode)

# end of main loop
