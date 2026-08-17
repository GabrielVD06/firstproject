import os

os.system('cls')

class Person:
  def __init__(self, fname, lname, id, age, gym):
    self.firstname = fname
    self.lastname = lname
    self.id = id
    self.age = age
    self.gym = gym


class Addres:
  def __init__(self, a):
    self.adduser = a


class Client(Person):
  def __init__(self, fname, lname, id, age, gym, sport):
    super().__init__(fname, lname, id, age, gym)
    self.sport = sport

class Worker(Person):
  def __init__(self, fname, lname, id, age, gym, workarea, salary):
    super().__init__(fname, lname, id, age, gym)
    self.area = workarea
    self.salary = salary

class Membership(Client):
  def __init__(self, fname, lname, id, age, gym, membership, sport):
    super().__init__(fname, lname, id, age, gym, sport)
    self.membership = membership
  def printclient(self):
    print(
      f"The client is {self.firstname} {self.lastname}, is {self.age} years old, have a membership \
{self.membership} for the gym {self.gym}, practice {self.sport} and the ID is {self.id}")
    
class Nofrecuent(Client):
  def __init__(self, fname, lname, id, age, gym, sport, classes):
    super().__init__(fname, lname, id, age, gym, sport)
    self.classes = classes
  def printclient(self):
    print(
      f"The client is {self.firstname} {self.lastname}, is {self.age} years old, have not a membership \
take {self.classes} unique classes in the gym {self.gym} at the month, practice {self.sport} and the ID is {self.id}")

class Salary(Worker):
  def __init__(self, fname, lname, id, age, gym, workarea, salary):
    super().__init__(fname, lname, id, age, gym, workarea, salary)
  def printwork(self):
    print(
      f"The worker is {self.firstname} {self.lastname}, is {self.age} years old, works on \
{self.area} area, works for the gym {self.gym}, the payment is {self.salary} and the ID is {self.id}")
    
check = (input('If you want to check the client introduce "1", if you want to check the worker introduce "2": '))
os.system('cls')

while check != "1" and check != "2":
  os.system('cls')
  check = (input('If you want to check the client introduce "1", if you want to check the worker introduce "2": '))

if check == "1":
  kind = input("The client have a membership (1) or take unique classes (2): ")
  os.system('cls')
  while kind != "1" and kind != "2":
    kind = input("The client have a membership (1) or take unique classes (2): ")
    os.system('cls')
  if kind == "1":
    client = Membership("Gabriel", "Villota", 1030000143, 19, "smarfit", "black", "swimming")
    client.printclient()
  if kind == "2":
    client = Nofrecuent("Gabriel", "Villota", 1030000143, 19, "smarfit", "swimming", 8)
    client.printclient()

if check == "2":
  worker = Salary("Juan", "Herrera", 202425800, 32, "bodytech", "training", 1500000)
  worker.printwork()