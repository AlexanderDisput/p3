
# Introduce the user to the password manager and its functionality 

# ask the user how long the password should be by entering a number between 8 - 40
#     validate that it is a number 
#     validate that it is between 8 - 40

# ask the user if he wants capital letters by entering y/n
#     validate that y or n was entered

# ask if the user wants numbers by entering y/n
#     validate y/n

# ask if the user wants to use symbols by entering y/n
#     validate y/n


# CONSTANTS: 
#     set of letters
#     set of symbols
#     set of numbers 


# create password function: 
#     set len of password to user input 
#     check what sets user wants to Use:
#         combine sets into a single list and randomize
#     loop through randomized list and append the amount of the user input password length 

# check if user is happy with the password:
#     no: 
#         randomize list again and return password list as string
#     yes:
#         return password list as string
    
# ask if user wants to randomize the order of the password
#     y:
#         randomize the password list and return as string 
#     n:
#         return password list as string 


# Additional functionality: 
#     connect Google Sheets API 
#     Ask user for account name/email relationship to created password
#     push email and password to sheet

#     Add a cryptographic layer to encrypt the data sent to doc 
#     add functionality to pull and decrypt information from doc 


def password_length():
    """
    Asks user for input of integer between 8 and 40.
    Try will validate if the input is an int and if the int is between 8 and 40
    """
    print("How long do you want your password to be? \n")

    while True:
        user_input = input("Please enter an NUMBER between 8 and 40\n")
        if validate_input(user_input):
            print("Input valid\n")
            break
    
    return user_input


def validate_input(user_password_length):
    """
    Checks the user input and confirms that it is an integer between 8 and 40
    """
    try:
        user_password_length = int(user_password_length)
    except ValueError:
        print(f"Invalid input! Must be an integer!\n")
        return False

    if not 8 <= user_password_length <= 40:
        print("Invalid input! Integer must be between 8 and 40\n")
        return False

    return True

password_length()

