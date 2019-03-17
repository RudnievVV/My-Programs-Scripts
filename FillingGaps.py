#! python3
# FillingGaps.py =  finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder
# and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt)
# and renames all the later files to close this gap.
# OUTPUT EXAMPLE:
#Renaming spam005.txt into spam004.txt
#Renaming spam006.txt into spam005.txt
#Renaming spam008.txt into spam006.txt
#Renaming spam010.txt into spam007.txt
#Renaming spam011.txt into spam008.txt
#Renaming spam015.txt into spam009.txt
#Renaming spam018.txt into spam010.txt
#Renaming spam099.txt into spam011.txt
#Renaming spam102.txt into spam012.txt
#Renaming spam555.txt into spam013.txt

import re, os, shutil

# Ask for the prefix and folder.
print('Enter file prefix and folder where to search.')
prefix = input('Prefix: ',)
folder = input('Folder: ',)
while True:
    if os.path.exists(folder) == True:
        if len(os.listdir(folder)) != 0:
            break
    folder = input('Please enter the existing folder with content to search: ',)

# Regex to search.
regPrefix = '^(' + prefix + ')'+'(.\d*)(.*)'
regPrefix = r'%s' % (regPrefix)
regSearch = re.compile(regPrefix)
regPrefixFor1st = '(' + prefix + ')' + '(.\d*)(.*)'
regPrefixFor1st = r'%s' % (regPrefixFor1st)
regSearchFor1st = re.compile(regPrefixFor1st)

# Search folder for files compare filenames and rename them filling the gap between both.
filenames = ' '.join(os.listdir(folder))

currentInt  = regSearchFor1st.search(filenames).group(2)
searchedInt = 0
for file in os.listdir(folder):
    fileSearch = regSearch.search(file)
    if fileSearch == None:
        continue
    else:
        searchedInt = fileSearch.group(2)
        if currentInt == searchedInt:
            continue
        else:
            LenSearchedInt = len(searchedInt)
            LenCurrentInt = len(currentInt)
            if int(searchedInt) == int(currentInt) + 1:
                currentIntInt = int(currentInt) + 1
                currentInt = str('0' * (LenCurrentInt - len(str(currentIntInt)))  + str(int(currentInt) + 1))
                continue
            else:
                currentIntInt = int(currentInt) + 1
                currentInt = str('0' * (LenCurrentInt - len(str(currentIntInt)))  + str(int(currentInt) + 1))
                printfile = prefix + (currentInt) + fileSearch.group(3)
                renamefile = prefix + (searchedInt) + fileSearch.group(3)
                print('Renaming ' + renamefile + ' into ' + printfile)
                shutil.move(os.path.join(folder, renamefile), os.path.join(folder, printfile))


        
