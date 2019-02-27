#! python3
# bulletPointsAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.


# input
#asd|12d|asd|12d
#asd|12d|asd|12d
#asd|12d|asd|12d
#asd|12d|asd|12d

# output
#*asd|*12d|*asd|*12d
#*asd|*12d|*asd|*12d
#*asd|*12d|*asd|*12d
#*asd|*12d|*asd|*12d


import pyperclip
text = pyperclip.paste()

# Separate lines and add starts.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)

lines = text.split('|')
for i in range(1, len(lines)):
    lines[i] = '*' + lines[i]
text = '|'.join(lines)

pyperclip.copy(text)
