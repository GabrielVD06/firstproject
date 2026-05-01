import datetime
import os

os.system('cls')

date = datetime.datetime.now()


print("1: Show the files")
print("2: Add a new file")
print("3: Edit a file")
print("4: Delete a file")
action = int(input("Write the action would you like to do: "))


while action < 1 or action > 4:
    os.system('cls')
    print("1: Show the files")
    print("2: Add a new file")
    print("3: Edit a file")
    print("4: Delete a file")
    action = int(input("Write the action would you like to do: "))

while action == 1:
    
    action = int(input("Write the action would you like to do: "))
    os.listdir(r"C:\Users\GABRIEL\Desktop\Files")
    print(os.listdir(r"C:\Users\GABRIEL\Desktop\Files"))
    os.system('cls')
    print("1: Show the files")
    print("2: Add a new file")
    print("3: Edit a file")
    print("4: Delete a file")

if action == 2:
    name = str(input("Write the name of your new file: "))
    new = open("C:/Users/GABRIEL/Desktop/Files/" + name + ".txt", "x")
    with open("C:/Users/GABRIEL/Desktop/Files/" + name + ".txt", "a") as new:
        new.write("Start here: ")


if action == 3:
    print("The files to modify: ")
    os.listdir(r"C:\Users\GABRIEL\Desktop\Files")
    print(os.listdir(r"C:\Users\GABRIEL\Desktop\Files"))
    name = str(input("Write the name of the file to modify: "))
    
    with open("C:/Users/GABRIEL/Desktop/Files/" + name, "a") as new:
        new.write("Modified by Gabriel at: " + str(date))
    with open("C:/Users/GABRIEL/Desktop/Files/" + name) as new:
        print(new.read())

if action == 4:
    print("The files to modify: ")
    os.listdir(r"C:\Users\GABRIEL\Desktop\Files")
    print(os.listdir(r"C:\Users\GABRIEL\Desktop\Files"))
    name = str(input("Write the name of the file to modify: "))
    if os.path.exists("C:/Users/GABRIEL/Desktop/Files/" + name):
        os.remove("C:/Users/GABRIEL/Desktop/Files/" + name)
    else:
        print("The file does not exist")
