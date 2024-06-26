# Custom Password Generator

This Python script provides a tool for creating secure and customizable passwords. It offers users the ability to specify the length of the password and whether to include capital letters, numbers, and symbols, ensuring that the generated passwords meet various security requirements.
It makes it simple to create a password and helps users maintain unique passwords for each platform with ease.

## Features

- **Customizable Password Length:** Users can specify the desired length of the password, allowing for a range between 8 and 40 characters.
  ![alt text](images/feature_pw_length.png)
- **Inclusion of Various Character Sets:** The script supports including capital letters, numbers, and symbols in the password for enhanced security.
  ![alt text](images/feature_capital_letters.png)

  ![alt text](images/feature_symbols.png)

  ![alt text](images/feature_numbers.png)


- **User-friendly Interaction:** Through a series of prompts, users can easily customize their password requirements.
 ![alt text](images/feature_ux.png)
- **Input validation:** Inputs given by users are validated to ensure full functionality.
 ![alt text](images/feature_validation.png)

## Requirements

- Python 3.x

This script does not depend on any external libraries, making it straightforward to run in any standard Python environment.

## Usage

To use the script, simply run it in a Python environment. 
Alternatively, you can open the deployed app on Heroku using: 
- **https://password-generator-p3-ca6c81b86e1a.herokuapp.com/**

The script will guide you through several prompts:

1. **Password Length:** Enter the desired length for your password (between 8 and 40 characters).
2. **Character Inclusions:** For each of the following - capital letters, symbols, and numbers - the script will ask if you wish to include them in your password. Respond with 'Y' for yes or 'N' for no.
3. **Password Regeneration:** After generating a password, you have the option to regenerate it using the same parameters or modify your preferences.

## Deployment & Local Development

### Deployment

The site is deployed using Heroku

# Game Deployment on Heroku

## Overview
This guide will walk you through the process of deploying our game to Heroku, a cloud platform that allows you to host and manage web applications.

## Prerequisites
Before you begin, make sure you have the following:
- A Heroku account. If you don't have one, you can sign up for free at [Heroku's website](https://www.heroku.com/).
- Git installed on your local machine. You can download Git from [here](https://git-scm.com/downloads).
- Basic knowledge of using the command line.

## Steps to Deploy
Follow these steps to deploy the game on Heroku:

1. **Clone the Repository:**
   ```
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory:**
   ```
   cd <project_directory>
   ```

3. **Create a Heroku App:**
   ```
   heroku create <app_name>
   ```

4. **Deploy the Code to Heroku:**
   ```
   git push heroku master
   ```

5. **Open the App:**
   ```
   heroku open
   ```

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [Random Password Generator](https://github.com/AlexanderDisput/p3)
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [Random Password Generator](https://github.com/AlexanderDisput/p3)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


## Testing

### PEP8 Report

My recent review of the Password Generator codebase for PEP8 compliance was positive, demonstrating commitment to maintaining high standards for readability and maintainability.

![alt text](images/pep8_test.png)

**Summary of Findings:**

- **Overall Compliance**: The code has successfully passed the PEP8 linter test, affirming our adherence to Python's style guide recommendations. This ensures that our code is not only functional but also clean and consistent, making it easier for developers to read, understand, and contribute to.


### Manual Tests

Below are the manual tests conducted to ensure the password generator script operates correctly, particularly in validating user inputs for password length, inclusion of character types, and handling of 'Y/N' responses.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Password Length Input | Accepts integers between 8 and 40 | Entered various numbers within and outside the range | Correctly accepts numbers within range and rejects those outside | Pass |
| Capital Letters Inclusion | Accepts 'Y' for yes and 'N' for no | Entered 'Y', 'N', and invalid inputs | Correctly processes 'Y' and 'N', rejects invalid inputs | Pass |
| Symbols Inclusion | Accepts 'Y' for yes and 'N' for no | Entered 'Y', 'N', and invalid inputs | Correctly processes 'Y' and 'N', rejects invalid inputs | Pass |
| Numbers Inclusion | Accepts 'Y' for yes and 'N' for no | Entered 'Y', 'N', and invalid inputs | Correctly processes 'Y' and 'N', rejects invalid inputs | Pass |
| Generating Password with All Options | Generates a password that matches specified criteria | Specified a set of criteria and generated a password | Password matches the criteria specified (length, inclusion of character types) | Pass |
| Handling of None Input | Rejects none input and prompts again | Attempted to press enter without typing anything | Prompted again for valid input | Pass |

These tests ensure that the script not only adheres to the user's customization preferences but also robustly handles unexpected or invalid input, maintaining usability and functionality.

### Additional Tests

##### Checked for correct validation. Please keep in mind that the validation is modular, meaning that failures in tests will apply to all other validation inputs i.e. if a number is accepted when a letter should be accepted, it will fail in every instance.

Tests include:
**Positive/negative integers**
**Empty space**
**Letters when numbers are required**
**Numbers when letters are required**
![alt text](images/input_testing_cap.png)
![alt text](images/input_testing_sym.png)
![alt text](images/input_testing_numb.png)
![alt text](images/input_testing_final_pw_ints.png)
![alt text](images/input_testing_final_pw_letters.png)


### Bugs Encountered and Resolution

### BUG 1: Endless Loop on Input Validation

**Issue:** The loop continues even after a valid integer is provided, without proper feedback to the user.

**Symptom:** 
```python
   while True:
        user_input = input("Please enter an NUMBER between 8 and 40\n")
        validate_input(user_input)
```

```python
Please enter an NUMBER between 8 and 40
9
Please enter an NUMBER between 8 and 40
```

**Resolution:** Ensure the loop exits upon valid input by checking the state returned by `validate_input` and using a `break` statement to exit the loop if input is valid.

```python
while True:
    user_input = input("Please enter an NUMBER between 8 and 40\n")
    if validate_input(user_input):
        print("Input valid")
        break
```

### BUG 2: Inaccessible Sublist in Password Elements List

**Issue:** When trying to create a list containing sublists of password elements like symbols and numbers, accessing the first list with `password[0]` returns the first letter of `BASE_LETTERS` instead of the expected sublist.

**Symptom:** 
```python
['e', 'w', 'i', 'v', 'r', 'q', 'x', 'p', 'k', 'h', 'g', 'a', 'y', 'f', 's', 'o', 'j', 'u', 'd', 'n', 'l', 'm', 'c', 'z', 'b', 't',[ ['B', 'N', 'H', 'P', 'I', 'X', 'C', 'D', 'K', 'T', 'U', 'V', 'J', 'G', 'M', 'Y', 'R', 'Z', 'S', 'E', 'A', 'O', 'Q', 'L', 'W', 'F'], ['[', ')', '~', '{', '`', '^', '<', '&', ',', ';', '-', ']', '?', '!', '@', "'", '"', '\\', '_', '|', '(', '$', '*', ':', '%', '+', '}', '/', '=', '.', '>', '#'], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']]
```

**Resolution:** The issue's root cause remains unclear to me, despite efforts to identify it. However, I suspect it is related to the use of the copy() method. As a workaround, I initiated an empty list with password = [] and then appended BASE_LETTERS to this list as follows:

```python
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
```

### BUG 3: Re-asking Parameters for New Password Generation

**Issue:** The application re-asks the user for parameters (symbols, numbers, etc.) when generating a new password, even if they wanted to use the same parameters.

```python
def main():
    while True:
        length = password_length()
        list_password_elements = user_password_pref()
        password = password_generator(list_password_elements, length)
        print(f"This is your password: {password}")
        user_choice = input("Would you like to generate a new password using the same parameters? Please answer with 'Y' OR 'N'\n")
        if user_choice.capitalize() != "Y":
            break
```

**Resolution:** Modify the main loop to avoid re-asking these parameters by storing the user's choices outside of the loop that generates the password.

```python
def main():
    while True:
        length = password_length()
        list_password_elements = user_password_pref()
        while True:
            password = password_generator(list_password_elements, length)
            print(f"\nThis is your password: {password}\n")
            user_choice = input("Would you like to generate a new password using the same parameters?\nPlease answer with 'Y' OR 'N'\n\n")
            if user_choice.capitalize() != "Y":
                break
        user_choice = input(f"\nAre you happy with your password:\n{password}?\n\nPlease answer with 'Y' OR 'N'\n\n")
        if user_choice.capitalize() == "Y":
            break
    print(f"\nYour final password is: {password}\n")
```

### BUG 4: Unrestricted Input for New Password Generation Prompt

**Issue:** The program accepts any input when asking the user if they want to generate a new password, leading to potential confusion or incorrect program flow.

```python
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
            user_choice = input("Would you like to generate a new password using the same parameters?\nPlease answer with 'Y' OR 'N'\n\n")
            if user_choice.capitalize() != "Y":
                break
        user_choice = input(f"\nAre you happy with your password:\n{password}?\n\nPlease answer with 'Y' OR 'N'\n\n")
        if user_choice.capitalize() == "Y":
            break
    print(f"\nYour final password is: {password}\n")
```

**Resolution:**  Implement a validation function that restricts the input to 'Y' or 'N', ensuring the program only proceeds with clear intent.

```python
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
```

### Additional Features that will be added:

- **Main Loop Optimization**: The main loop can be streamlined for efficiency, with a focus on reducing the verbosity of the while loops. The approach to gathering user input can be made more modular, enhancing the code's readability and maintainability.

- **Google Sheets Integration**: The application now could include functionality to connect with Google Sheets. Users can provide their email or chosen platform, which the application then records in a Google Sheets document. This feature enables easy tracking and management of passwords across different platforms.

- **Encryption Algorithm**: To ensure the security of stored passwords, an encryption algorithm can been implemented. This algorithm encrypts passwords before they are pushed to the Google Sheets file. The addition of this feature enhances the application's security, protecting sensitive information from potential vulnerabilities.

- **Functionality Division**: The application could offer users the choice between creating a new password or retrieving data from the file. For data retrieval, the application decrypts the information, ensuring that users can access their stored passwords.


### Credits:

Exclusively used the online resources of Code Institute
All written code was written by me