import os
os.system("cls")


class Carro:
  id = 5
  marca = "bmw"


c1 = Carro()
print(c1.marca)
c1.marca = "porsche"
print(c1.marca)

class Person:
  def __init__(hello, name):
    hello.name= name

  def __init__(hello, name, age=18):
    hello.name = name
    hello.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil")
p2 = Person("Tobias",20)

print(p1.name, p1.age)
print(p2.name, p2.age)
p1.greet()
p2.greet()

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()


class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! {self.name}, you are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
[p1.celebrate_birthday(), p1.celebrate_birthday()]