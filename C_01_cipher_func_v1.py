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


def encode(text, shift):
    '''Encodes text by shift amount'''

    result = ""

    for char in text:

        if char in alphabet:
            shifted_position = alphabet.index(char) + shift
            shifted_position = shifted_position % len(alphabet)
            result = result + alphabet[shifted_position]

        else:
            result += char
    
    print("Encrypted Message: ", result)


def decode(text, shift):
    '''Decrypts text with known shift amount'''

    shift = shift * -1
    result = ""

    for char in text:

        if char in alphabet:
            shifted_position = alphabet.index(char) + shift
            shifted_position = shifted_position % len(alphabet)
            result = result + alphabet[shifted_position]

        else:
            result += char

    print("Decrypted Message: ", result)



# main

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    
    mode = string_check("Encrypt or Decrypt? ", ['encrypt', 'decrypt', 'xxx'])
    print()

    if mode == 'xxx':
        break

    elif mode == "encrypt":
        text = input("Plain text: ")
        print()
        shift = int_check("Shift amount: ")
        print()
        encode(text, shift)
        print()

    else:
        text = input("Cipher Text: ")
        decrypted_messages = ""
        print()
        shift = int_check("Shift amount: ")
        print()
        decode(text, shift)
        print()


# end of main loop
