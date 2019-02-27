#! python3
# function that takes a string and does the same thing as the strip() string method

import re

print('Please enter the value:', end='')
word = input()
def RegexVersionOfStrip(word):
    noSpace = re.compile(r'\S')
    print(''.join(noSpace.findall(word)))

RegexVersionOfStrip(word)
