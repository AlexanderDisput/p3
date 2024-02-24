# Custom Password Generator

This Python script provides a tool for creating secure and customizable passwords. It offers users the ability to specify the length of the password and whether to include capital letters, numbers, and symbols, ensuring that the generated passwords meet various security requirements.

## Features

- **Customizable Password Length:** Users can specify the desired length of the password, allowing for a range between 8 and 40 characters.
- **Inclusion of Various Character Sets:** The script supports including capital letters, numbers, and symbols in the password for enhanced security.
- **User-friendly Interaction:** Through a series of prompts, users can easily customize their password requirements.
- **Input validation:** Inputs given by users are validated to ensure full functionality.

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

## Testing

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

### Bugs Encountered and Resolution

### BUG 1: Endless Loop on Input Validation

**Issue:** The loop continues even after a valid integer is provided, without proper feedback to the user.

**Symptom:** 
Please enter an NUMBER between 8 and 40
9
Please enter an NUMBER between 8 and 40


**Resolution:** Ensure the loop exits upon valid input by checking the state returned by `validate_input` and using a `break` statement to exit the loop if input is valid.

```python
while True:
    user_input = input("Please enter an NUMBER between 8 and 40\n")
    if validate_input(user_input):
        print("Input valid")
        break

Fixed the error message by using an f-string and refining the ValueError handling for more precise user feedback.

