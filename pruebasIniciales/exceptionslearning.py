try:
  print(x)
except:
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

value = -1
condition = True

while (value < 0 or value > 3) or condition == True:
  condition = False
  try:
    value = int(input("Write a number on range 0 to 4: "))
  except:
      condition = True
  else:
    condition = False

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
