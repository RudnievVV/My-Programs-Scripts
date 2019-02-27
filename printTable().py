tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(colWidths)):
        colWidths[i] = len(' '.join(tableData[i]))
    for i in tableData:
        print(' '.join(i).rjust(max(colWidths)))
printTable()
