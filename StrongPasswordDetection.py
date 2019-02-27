#! python3
# StrongPasswordDetection.py - A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit.

import re

def StrongPasswordDetection():
    passUpperRegex = re.compile(r'[A-Z]')
    passLowerRegex = re.compile(r'[a-z]')
    passDigitRegex = re.compile(r'[0-9]')
    while True:
        print("Enter password for verification:", end='')
        password = input()
        if len(password) < 8:
            print('Password is too short, no less than 8 characters.')
        if passUpperRegex.search(password) == None:
            print('Password must contain both uppercase and lowercase characters.')
        if passLowerRegex.search(password) == None:
            print('Password must contain both uppercase and lowercase characters.')
        if passDigitRegex.search(password) == None:
            print('Password must contain atleast 1 digit.')
        allCondsAreOK = (
            len(password) >= 8 and
            passUpperRegex.search(password) != None and
            passLowerRegex.search(password) != None and
            passDigitRegex.search(password) != None
            )
        if allCondsAreOK:
            break
    print('Password is strong.')

StrongPasswordDetection()
