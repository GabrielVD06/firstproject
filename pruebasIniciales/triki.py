import os

def checkPos(check: list, fila: int, columna: int) -> bool :
    base = False
    if str(check[fila][columna]) == "[-]":
        base = True
    return(base)



rows = 3
col = 3

matrix = [] 
os.system('cls')
for i in range(rows):   
    row = []
    for j in range(col):
        row.append("[-]")   
    matrix.append(row)  


fila = 0
columna = 0
count = 0
user = 1
comprove = False

while count < 9 and comprove == False:
    print("triki matrix")
    for x in range(rows):
        for y in range(col):
            print(matrix[x][y], end=" ")
        print()

    if user == 1:
        playerName = "Player 1"
    if user == 2:
        playerName = "Player 2"

    fila = int(str(input(playerName + " introduce the row: ")))
    while fila < 0 or fila > 2 :
        #os.system('cls')
        fila = int(str(input(playerName + " introduce a possible row: ")))

    columna = int(str(input(playerName + " introduce the col: ")))
    while columna < 0 or columna > 2 :
            #os.system('cls')
        columna = int(str(input(playerName + " introduce a possible col: ")))
    
         


    while checkPos(matrix, fila, columna) == False:
        print("triki matrix")
        for x in range(rows):
            for y in range(col):
                print(matrix[x][y], end=" ")
            print()
        fila = int(str(input(playerName +  " introduce another row: ")))
        while fila < 0 or fila > 2 :
                #os.system('cls')
            fila = int(str(input(playerName + " introduce another row: ")))

        columna = int(str(input(playerName + " introduce another col: ")))
        while columna < 0 or columna > 2 :
                #os.system('cls')
            columna = int(str(input(playerName + " introduce another col: ")))
    
    os.system('cls')
    if user == 1:
        matrix[fila][columna] = "[X]"
        user = 2
    elif user == 2:
        matrix[fila][columna] = "[O]"
        user = 1
    count += 1
    for i in range(rows):   
        a = matrix[i][0]
        b = matrix[i][1]
        c = matrix[i][2]
        if (str(a) == "[X]" or str(a) == "[O]") and a == b and a == c:
            comprove = True
    for i in range(rows):   
        a = matrix[0][i]
        b = matrix[1][i]
        c = matrix[2][i]
        if (str(a) == "[X]" or str(a) == "[O]") and a == b and a == c:
            comprove = True
    val0 = matrix[0][0]
    val1 = matrix[0][2]
    val2 = matrix[1][1]
    val3 = matrix[2][0]
    val4 = matrix[2][2]
    
    if (str(val0) == "[X]" or str(val0) == "[O]") and val0 == val2 and val0 == val4:
        comprove = True
    if (str(val1) == "[X]" or str(val1) == "[O]") and val1 == val2 and val1 == val3:
        comprove = True


print("triki matrix")
for x in range(rows):
    for y in range(col):
        print(matrix[x][y], end=" ")
    print()
if comprove == True :
    print(playerName + " won the game")
else :
    print("Draw")