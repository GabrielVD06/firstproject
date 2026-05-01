n = int(input("Valor del conteo: "))
x = ""
y = 1
while y < n+1:
    x += str(y)
    y += 1
print(x)


m = int(input("Valor del conteo: "))
z = -1
count = [m]
while z < m-1 :
    z = z+1
    count.insert(-1,z)
    print(count[z]**2)


year = int(input("Año: "))
leap = False
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    leap = True
print(leap)


