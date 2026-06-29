# Functions
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


def instructions():
    '''Prints instructions'''
    print('''

---Instructions---
          
- First, choose either encrypt or decrypt.
- Next, enter the plain / cipher text.
- If you have chosen encrypt, choose an amount to shift.
- You will then see the encrypted / decrypted text.
- To exit the code, choose xxx instead of encrypt / decrypt.
    ''')


def cipher_func(mode):
    '''Encrypts/Decrypts user input'''

    CHAR_RANGE = 26

    result = ''

    if mode == "encrypt":
        # Get plain text, and save it,
        # and get shift amount (between 0 and 26) using int_check func
        text = input("Plain text: ")
        print()
        shift = int_check("Shift amount: ")
        print()
        un_encrypted_messages.append(text)

    elif mode == 'decrypt':
        # Get cipher text and save it
        text = input("Cipher Text: ")
        decrypted_messages = ""
        print()
        shift = 25
        un_decrypted_messages.append(text)
    
    else:
        return

    while shift > 0:

        for char in text:

            # Checks if letter is upper/lowercase
            if char.isupper():
                FIRST_CHAR_CODE = 65
                LAST_CHAR_CODE = 90

            if char.islower():
                FIRST_CHAR_CODE = 97
                LAST_CHAR_CODE = 122

            # Convert letter to ASCII code, shift it, convert back to char
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

        # For decrypt, decrease shift and go again until shift is zero, save all results
        if mode == 'decrypt':
            print(f"Shift {26-shift}: {result}")
            decrypted_messages += result + ', '
            result = ""
            shift -= 1
        # For encrypt, break function, save result
        if mode == 'encrypt':
            print(f"Encrypted Text: {result}\n")
            encrypted_messages.append(result)
            break

    # Save decrypt results to list
    if mode == 'decrypt':
        decrypted_messages = decrypted_messages[:-2]
        decrypted_messages_lists.append(decrypted_messages)
        decrypted_messages = ""
    print()


# Main Routine

# Initialise lists
un_encrypted_messages = []
encrypted_messages = []
un_decrypted_messages = []
decrypted_messages_lists = []

# Program heading
print("\n=== Caesar Cipher Encrypter & Decrypter ===\n")

# Ask user if they want to see the instructions
# display them if necessary
instruction = string_check("Would you like to see the instructions? ", ['yes', 'no'])

if instruction == 'yes':
    instructions()

print()

# Loop cipher function until user inputs exit code
while True:

    # Check if user wants to encrypt or decrypt
    mode = string_check("Encrypt or Decrypt? ", ['encrypt', 'decrypt', 'xxx'])
    print()

    if mode == 'xxx':
        break

    cipher_func(mode)

# End of cipher loop

# Show history (if avaliable)
if len(un_encrypted_messages) > 0:

    # Encrypted Messages Heading
    print("---Encrypted Messages---\n")

    # Print each unencrypted message with its encrypted version
    for item in un_encrypted_messages:
        index = un_encrypted_messages.index(item)
        print(f'{item} --> {encrypted_messages[index]}\n')

if len(un_decrypted_messages) > 0:

    # Decrypted Messages Heading
    print("---Decrypted Messages---\n")

    # Print each undecrypted message with all of its possible solutions
    for item in un_decrypted_messages:
        index = un_decrypted_messages.index(item)
        print(f'{item}: \n\n{decrypted_messages_lists[index]}\n')
