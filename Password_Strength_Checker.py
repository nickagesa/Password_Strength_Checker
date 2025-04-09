# Simple Python script to check the strength of a password.

import string # This module provides constants and classes for working with string data.
# It provides a set of ASCII characters, including digits, lowercase and uppercase letters, and punctuation symbols.


def check_password_strength(password):
    strength = "Weak" # Initialize the strength variable to "Weak"
    if (len(password) >= 8 and 
        any(c.isupper() for c in password) and  
        any(c.isdigit() for c in password) and  
        any(c in string.punctuation for c in password)): # Check if the password is at least 8 characters long,contains at least one uppercase letter, one digit, and one special character
        
        strength = "Strong" # If the password meets the criteria, set strength to "Strong"
    else:
        strength = "Weak" # If the password does not meet the criteria, set strength to "weak"
    
    print(f"Password Strength: {strength}")

    '''If statement break down:
    # len() is a function that returns the length of an object. In this case, it returns the length of the password.
    # any() is a function that returns True if any element of an iterable(eg. list, string) is True.
    # c is a variable that represents each character in the password.
    # c.isupper() returns True if c is an uppercase letter.
    # c.isdigit() returns True if c is a digit.
    # for c in password is a generator expression that iterates through each character in the password.
    # string.punctuation is a string that contains all punctuation symbols. eg. !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # c in string.punctuation returns True if c is a punctuation symbol.
    '''
# Prompt the user for a password
def user_input():
    password = input("Enter a password: ") 
    check_password_strength(password) # Call the check_password_strength function with the password as an argument

user_input() # Call the user_input function

