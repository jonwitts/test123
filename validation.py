def valid_number(message):
    not_valid = True  # input has not been validated
    while not_valid:
        print(message)  # display message parameter
        try:
            number = int(input())  # try to convert to integer
            not_valid = False  # if successful then set data as validated
        except ValueError:
            print("Please enter a number!")  # int() failed - prompt to re-enter a number
    return number  # return valid number