value = 0
while value < 10 :
    #print(value)
    value += 1
    if value == 2:
        continue
print (value)


num = int(input("Digite un valor: "))
cont = num
val = 0
while cont > 0 :
    if num % cont == 0 :
            val += 1
    cont -= 1
if val == 2: 
        print(True)
else: print(False)


n = int(input("Valor del conteo: "))
x = ""
y = 1
while y < n+1:
    x += str(y)
    y += 1
print(x)

