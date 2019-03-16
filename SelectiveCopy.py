#! python3
# SelectiveCopy.py - searches and copies .txt and .jpg files from a folder to specified folder,
# adding file foldername to the filename to make it unique and specify from where file is copied.

import os, shutil

# Ask User to specify a folders where to search for files and to which folder copy found files.
print('Please specify the existing folder where to search for .txt and .jpg files.')
while True:
    folderFrom = input()
    if os.path.exists(folderFrom) == True:
        if len(os.listdir(folderFrom)) != 0:
            break
    print('Please enter the existing folder with content to search.')
print('Please specify the folder to copy in the found files.\nIf folder doesn\'t exist, it will be created.')
folderTo = input()
if os.path.exists(folderTo) == False:
    os.makedirs(folderTo)
    
# Make program to walk through the folder to search files and 
# make program to copy found files to specified folder.
for foldername, subfolders, filenames in os.walk(folderFrom):
    for filename in filenames:
        if foldername == folderTo:
            continue
        if filename.endswith('.txt') or filename.endswith('.jpg'):
            #print('Copying ' + '"' + os.path.join(foldername, filename) + '" to ' + '"' + os.path.join(folderTo, os.path.basename(foldername) + '-' + filename) + '"')
            shutil.copy(os.path.join(foldername, filename), os.path.join(folderTo, os.path.basename(foldername) + '-' + filename))
        

print('Done')

