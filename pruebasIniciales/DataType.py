#Text 
 #str = "Hello world" 
#Numeric
 #int = 10 
 #float = 5.5 
 #complex = 2j
#Sequence
 #list = ["Manzana", 21, True] 
 #tuple = ("apple", "banana", "cherry")
 #range = range(6)
#Mapping
 #dict = {"Name": "Gabriel", "Age": 19}
#Set
 #set = {"apple", "banana", "banana"}
 #frozenset = frozenset({"apple", "banana", "cherry"})
#Boolean
 #bool = True or False
#Binary
 #bytes = b"Hello"
 #bytearray = bytearray(5)
 #memoryview = memoryview(bytes(5))
#None Type
 #NoneType = None
num2 = 19
num = 19
name = "Gabriel"
print(name + " tiene " + str(num) + " años, lo que equivale a " + str(num*12) + " meses")
print("abc is", bool("abc")) #why true? And why "abc" == True = False?
print("Any value different to 0", "is", bool(1), "and 0 is", bool(0)) # X != 0 = True
print("None is", bool(None)) # None = False
print(bool(num is num2))
print(num < 15)
print(num != 15)
# any() returns False if all into () are False
# all() returns True if all into () are True