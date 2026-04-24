def winner(rev: list) -> bool :
    result = False
    if str(rev[0][2]) == "[X]" or str(rev[1][2]) == "[X]" or str(rev[2][2]) == "[X]" or str(rev[2][0]) == "[X]" or str(rev[2][1]) == "[X]" or str(rev[2][2]) == "[X]":
        result = True
    if str(rev[0][2]) == "[O]" or str(rev[1][2]) == "[O]" or str(rev[2][2]) == "[O]" or str(rev[2][0]) == "[O]" or str(rev[2][1]) == "[O]" or str(rev[2][2]) == "[O]":
       result = True
    return(result)

rows = 3
col = 3

matrix = [] 
os.system('cls')
for i in range(rows):   
    row = []
    for j in range(col):
        row.append("[-]")   
    matrix.append(row)



rows = 3
col = 3


for i in range(rows):   
    x = matrix[i,0]
    y = matrix[i,1]
    z = matrix[i,2]
    if x == y and x == z:
        break
for i in range(rows):   
    x = matrix[0,i]
    y = matrix[1,i]
    z = matrix[2,i]
    if x == y and x == z:
        break
