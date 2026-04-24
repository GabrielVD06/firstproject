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
while count < 9 :
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
        if a == b and a == c:
            break
    for i in range(rows):   
        x = matrix[0][i]
        y = matrix[1][i]
        z = matrix[2][i]
        if a == b and a == c:
            break

print("triki matrix")
for x in range(rows):
    for y in range(col):
        print(matrix[x][y], end=" ")
    print()
print(playerName + " won the game")