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

while True:
    int_check('Shift: ')
    print()