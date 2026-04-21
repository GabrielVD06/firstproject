firstlist = ["carro", "moto", "avion"]
print(firstlist)
secondlist = ["carro", "moto", "avion", "carro"]
print(len(secondlist))
bool_list = [True, True, False, True]
print(bool_list)
num_list = [5, 6, 9, 21, 3, 4]
print(num_list)
multi_list = [True, "carro", 2, 3, False, "moto"]
print(multi_list)
print(type(multi_list))
command = list(("gato", "perro", "loro", "perro"))
print(command[2])
print(num_list[-1])
print(num_list[2:5])
num1_list = [1, 2, 8, 12, 5, 6]
print(num1_list)
num1_list[2:4] = [3, 4]
num1_list.append(7)
print(num1_list)
firstlist.extend(secondlist)
print(firstlist)