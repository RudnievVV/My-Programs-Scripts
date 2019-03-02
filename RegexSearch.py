#! python3
# RegexSearch - program that opens all .txt files in a folder and searches for
# any line that matches a user-supplied regular expression. The results are going be printed to the screen.

import os, re

# Ask user for variable to search.
print('Enter the variable to search:')
Variable = input(r'')
VariableRegex = re.compile(Variable) #optional to use regex, I will not use it

# Ask user for a folder to check for .txt files.
print('Enter folder path where to search:')
path = input()
while True:
    if os.path.isdir(path) != False:
        break
    else:
        print('Please check folder path and enter again')

# Open each .txt file and search for variable and print the result.
for file in os.listdir(path):
    try:
        if file[file.index('.txt'):file.index('.txt')+4] == ".txt":
            openedFile = open(os.path.join(path, file))
            openedFileContent = openedFile.readlines()
            openedFile.close()
            n = 0
            for i in openedFileContent:
                if Variable in openedFileContent[n]:
                    print(openedFileContent[n])
                n = n + 1
    except ValueError:
        continue

