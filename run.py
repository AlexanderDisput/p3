import random

BASE_LETTERS = ['e', 'w', 'i', 'v', 'r', 'q', 'x', 'p', 'k', 'h', 'g', 'a', 'y', 'f', 's', 'o', 'j', 'u', 'd', 'n', 'l', 'm', 'c', 'z', 'b', 't']
CAPITAL_LETTERS = ['B', 'N', 'H', 'P', 'I', 'X', 'C', 'D', 'K', 'T', 'U', 'V', 'J', 'G', 'M', 'Y', 'R', 'Z', 'S', 'E', 'A', 'O', 'Q', 'L', 'W', 'F']
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
SYMBOLS = ['[', ')', '~', '{', '`', '^', '<', '&', ',', ';', '-', ']', '?', '!', '@', "'", '"', '\\', '_', '|', '(', '$', '*', ':', '%', '+', '}', '/', '=', '.', '>', '#']

def password_length():
    """
    Asks user for input of integer between 8 and 40.
    Try will validate if the input is an int and if the int is between 8 and 40
    """
    print("How long do you want your password to be? \n")
    while True:
        user_input = input("Please enter an NUMBER between 8 and 40\n\n")
        if validate_password_length(user_input):
            print("\nInput valid\n")
            break
    return int(user_input)

def validate_password_length(user_password_length):
    """
    Checks the user input and confirms that it is an integer between 8 and 40
    """
    try:
        user_password_length = int(user_password_length)
    except ValueError:
        print(f"\nInvalid input! Must be an integer!\n")
        return False
    if not 8 <= user_password_length <= 40:
        print("\nInvalid input! Integer must be between 8 and 40\n")
        return False
    return True
