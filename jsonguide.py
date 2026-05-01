import json
import os
os.system('cls')

print("json to Python")

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

print("Python to json")

x = {"name": "John","age": 30,"city": "New York"}
y = json.dumps(x)
print(y)

