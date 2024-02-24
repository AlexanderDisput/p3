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

def validate_binary_question(user_answer):
    """
    Checks if the users answer to Yes/No question is valid given that it must be Y or N
    """
    if user_answer.capitalize() == "Y" or user_answer.capitalize() == "N":
        print("\nInput valid\n")
        return True
    else:
        print(f"Your input {user_answer} is invalid!\nPlease enter 'Y' OR 'N'\n")
        return False

def user_password_requirements(type):
    """
    Checks if user wants to enable certain requirements
    such as capital letters, numbers and symbols
    """
    while True:
        user_choice = input(f"Do you want to use {type} in your password?\nPlease answer with 'Y' OR 'N'\n\n")
        if validate_binary_question(user_choice):
            break
    return user_choice.capitalize()

def user_password_pref():
    """
    Asks user if they want symbols, capital letters and numbers in their password
    returns 
    """
    password = []
    password.append(BASE_LETTERS)
    if user_password_requirements("capitalized letters") == "Y":
        password.append(CAPITAL_LETTERS)
    if user_password_requirements("symbols") == "Y":
        password.append(SYMBOLS)
    if user_password_requirements("numbers") == "Y":
        password.append(NUMBERS)
    return password

def password_generator(password_elements, password_length_as_int):
    """
    Creates a random password with random number generator
    Each for loop creates a new random number. 
    parent_choice is a random choice of LETTERS, NUMBERS or SYMBOLS
    sublist is a random choice within those lists
    """
    password = ""
    for i in range(password_length_as_int):
        parent_list = random_number_generator(len(password_elements))
        sublist = random_number_generator(len(password_elements[parent_list]))
        password += password_elements[parent_list][sublist]
    return password

def random_number_generator(max_random_num):
    """
    Creates a random number within the max_random_num, 
    which will be the length of the list we provide as argument
    """
    random_num = random.randint(0, max_random_num-1)
    return random_num

def main():
    """
    Setup for program order which asks the user if they want to 
    change the password using the same parameters or create a completely new set of parameters
    """
    while True:
        length = password_length()
        list_password_elements = user_password_pref()
        while True:
            password = password_generator(list_password_elements, length)
            print(f"\nThis is your password: {password}\n")
            while True:
                user_choice = input("Would you like to generate a new password using the same parameters?\nPlease answer with 'Y' OR 'N'\n\n")
                if validate_binary_question(user_choice):
                    break  
            if user_choice.capitalize() != "Y":
                break  
        while True:
            user_choice = input(f"\nAre you happy with your password:\n{password}?\n\nPlease answer with 'Y' OR 'N'\n\n")
            if validate_binary_question(user_choice):
                break  
        if user_choice.capitalize() == "Y":
            break  
    print(f"\nYour final password is: {password}\n")

main()