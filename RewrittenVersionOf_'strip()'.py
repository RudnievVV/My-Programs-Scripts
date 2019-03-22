#! python3
# RewrittenVersionOf_'strip()'.py - does the same as strip() function without using regexes.


# Ask user for variables.
string = input('Enter the string:',)
value = input('Enter the value or leave blank:',)
if value == '':
    value = ' \r\n\t'
stringList = list(string)
valueList = list(value)

# Cut the string beginning.
while True:
    for i in valueList:
        if i in string and i == stringList[0]:
            del stringList[0]
        if i in string and i != stringList[0]:
            continue
    if stringList[0] not in valueList:
        break
stringList.reverse()

# Cut the string ending.
while True:
    for i in valueList:
        if i in string and i == stringList[0]:
            del stringList[0]
        if i in string and i != stringList[0]:
            continue
    if stringList[0] not in valueList:
        break
stringList.reverse()

stringList = ''.join(stringList)

# Print the output.
print('Output:' + stringList)
