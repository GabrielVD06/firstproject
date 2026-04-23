import os

def checkPos(check: list, fila: int, columna: int) -> bool :
    base = True
    #if str(check[fila][columna]) != "[-]":
        #base = False
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

print("triki matrix")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()

count = 0
user = 1
while count < 9 :

    if user == 1:
        fila = int(str(input("Player 1, introduce the row: ")))
        while fila < 0 or fila > 2 :
            #os.system('cls')
            fila = int(str(input("Player 1, introduce a possible row: ")))

        columna = int(str(input("Player 1, introduce the col: ")))
        while columna < 0 or columna > 2 :
            #os.system('cls')
            columna = int(str(input("Player 1, introduce a possible col: ")))
    
        os.system('cls')

        for i in range(rows):   
            row = []
            for j in range(col):
                row.append("[-]")   
            matrix.append(row)
            matrix[fila][columna] = "[x]" 


        while checkPos(matrix, fila, columna) == True:
            print("triki matrix")
            for x in range(rows):
                for y in range(col):
                    print(matrix[x][y], end=" ")
                print()
            fila = int(str(input("Player 1, introduce another row: ")))
            while fila < 0 or fila > 2 :
                #os.system('cls')
                fila = int(str(input("Player 1, introduce another row: ")))

            columna = int(str(input("Player 1, introduce another col: ")))
            while columna < 0 or columna > 2 :
                #os.system('cls')
                columna = int(str(input("Player 1, introduce another col: ")))
    
            os.system('cls')

            for i in range(rows):   
                row = []
                for j in range(col):
                    row.append("[-]")   
                matrix.append(row)
        user = 0

        print("triki matrix")
        for x in range(rows):
            for y in range(col):
                print(matrix[x][y], end=" ")
            print()
        count += 1

    if user == 0:
        fila = int(str(input("Player 2, introduce the row: ")))
        while fila < 0 or fila > 2 :
            #os.system('cls')
            fila = int(str(input("Player 2, introduce a possible row: ")))

        columna = int(str(input("Player 2, introduce the col: ")))
        while columna < 0 or columna > 2 :
            #os.system('cls')
            columna = int(str(input("Player 2, introduce a possible col: ")))
    
        os.system('cls')

        for i in range(rows):   
            row = []
            for j in range(col):
                row.append("[-]")   
            matrix.append(row)
            matrix[fila][columna] = "[O]" 
            user = 0


        while checkPos(matrix, fila, columna) == True:
            fila = int(str(input("Player 2, introduce another row: ")))
            while fila < 0 or fila > 2 :
                #os.system('cls')
                fila = int(str(input("Player 2, introduce another row: ")))

            columna = int(str(input("Player 2, introduce another col: ")))
            while columna < 0 or columna > 2 :
                #os.system('cls')
                columna = int(str(input("Player 2, introduce another col: ")))
    
            os.system('cls')

            for i in range(rows):   
                row = []
                for j in range(col):
                    row.append("[-]")   
                matrix.append(row)
        user = 1
        

        print("triki matrix")
        for x in range(rows):
            for y in range(col):
                print(matrix[x][y], end=" ")
            print()
        count += 1     