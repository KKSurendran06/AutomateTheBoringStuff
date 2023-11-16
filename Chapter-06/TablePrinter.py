
def printTable(data):
    row = len(data[0]) 
    column = len(data)
    colWidths = [0] * column
    
    for i in range(column):
        for j in range(row):
            if len(data[i][j]) > colWidths[i]:
                colWidths[i] = len(data[i][j])
            
    
    for i in range (row):
        for j in range (column):
            print((data[j][i]).rjust(colWidths[j]+1), end="")
        print("")     
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)    