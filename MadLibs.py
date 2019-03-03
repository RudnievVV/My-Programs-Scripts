#! python3
# MadLibs.py -  reads in text files and lets the user add their own text anywhere
#               the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
# Input example: "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
# Output example: "The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events."

import re, os

# Make program to read text file and save the value for future usage.
while True:
    print('Enter the file path:')
    inputFilePath = input()
    if os.path.exists(inputFilePath) != False:
        break
    else:
        print('File does not exist. Please check the path and try again')
FileContentTemp = open(inputFilePath, 'r')
FileContent = FileContentTemp.read()
FileContentTemp.close()

# Create regexes for variables.
AdjectiveRegex = re.compile(r'ADJECTIVE')
AdjectiveSearch = AdjectiveRegex.search(FileContent)

NounRegex = re.compile(r'NOUN')
NounSearch = NounRegex.search(FileContent)

AdverbRegex = re.compile(r'ADVERB')
AdverbSearch = AdverbRegex.search(FileContent)

VerbRegex = re.compile(r'VERB')
VerbSearch = VerbRegex.search(FileContent)

# Create rules for search.
AllCond = (AdjectiveRegex.search(FileContent), NounRegex.search(FileContent), AdverbRegex.search(FileContent), VerbRegex.search(FileContent))
allCondsAreOK = (AdjectiveRegex.search(FileContent) == None and
                 NounRegex.search(FileContent) == None and
                 AdverbRegex.search(FileContent) == None and
                 VerbRegex.search(FileContent) == None)

# Let user to enter their own variables and replace the variables.
while True:
    if allCondsAreOK == True:
        print('Nothing to check')
        break
    if AllCond != None:
        if AdjectiveRegex.search(FileContent) != None:
            print('Enter a adjective:')
            AdjectiveSub = input()
            FileContent = FileContent[:FileContent.index(AdjectiveSearch.group())] + AdjectiveSub + FileContent[FileContent.index(AdjectiveSearch.group()) + len('ADJECTIVE'):]
        if NounRegex.search(FileContent) != None:
            print('Enter a noun:')
            NounSub = input()
            FileContent = FileContent[:FileContent.index(NounSearch.group())] + NounSub + FileContent[FileContent.index(NounSearch.group()) + len('NOUN'):]
        if AdverbRegex.search(FileContent) != None:
            print('Enter a adverb:')
            AdverbSub = input()
            FileContent = FileContent[:FileContent.index(AdverbSearch.group())] + AdverbSub + FileContent[FileContent.index(AdverbSearch.group()) + len('ADVERB'):]
        if VerbRegex.search(FileContent) != None:
            print('Enter a verb:')
            AdverbSub = input()
            FileContent = FileContent[:FileContent.index(VerbSearch.group())] + AdverbSub + FileContent[FileContent.index(VerbSearch.group()) + len('VERB'):]
            
        if allCondsAreOK:
            print(FileContent)
            break

# Print the result.
# Program will print the result whenether found needed variables or not.
