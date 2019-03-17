#! python3
# DeletingUnneededFiles.py -  walks through a folder tree and searches
# for exceptionally large files(100 MB) and removes them asking before remove or not.

import os, send2trash

# Ask for folder to search.
folder = input('Enter the folder to search: ',)
while True:
    if os.path.exists(folder) == True:
        if len(os.listdir(folder)) != 0:
            break
    folder = input('Please enter the existing folder with content to search: ',)

# Search folder for files, ask to remove file or not if it is equals or larger 100MB.
for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            if os.path.getsize(os.path.join(foldername,file)) >= 104857600:
                print('Size of ' + os.path.join(foldername,file) + ' is - ' + str(os.path.getsize(os.path.join(foldername,file))))
                answer = input('Enter y/n to remove file or not: ',).lower()
                while True:
                    if answer == 'y':
                        print('Removing ' + os.path.join(foldername,file))
                        #os.unlink(os.path.join(foldername,file)) # uncomment after testing
                        send2trash.send2trash(os.path.join(foldername,file))
                        break
                    if answer == 'n':
                        print('Skipping file')
                        break
                    if answer != 'y' or 'n':
                        answer = input('Enter y/n: ',).lower()
                        continue

print('Done')
                
