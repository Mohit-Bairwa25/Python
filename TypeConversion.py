# Program to demonstrate Type Conversion in Python

# Integer
num = 10

# Float
decimal = 15.75

# String
text = "25"

# Boolean
flag = True

print("Original Values")
print("Integer :", num)
print("Float   :", decimal)
print("String  :", text)
print("Boolean :", flag)

print("\n----- Type Conversion -----")

# int() Conversion
print("int(decimal) =", int(decimal))
print("int(flag)    =", int(flag))

# float() Conversion
print("float(num)   =", float(num))
print("float(text)  =", float(text))
print("float(flag)  =", float(flag))

# str() Conversion
print("str(num)     =", str(num))
print("str(decimal) =", str(decimal))
print("str(flag)    =", str(flag))

# bool() Conversion
print("bool(num)    =", bool(num))
print("bool(0)      =", bool(0))
print("bool(text)   =", bool(text))
print("bool('')     =", bool(""))

# List Conversion
numbers = (1, 2, 3, 4)
print("list(tuple)  =", list(numbers))

# Tuple Conversion
fruits = ["Apple", "Banana", "Mango"]
print("tuple(list)  =", tuple(fruits))

# Set Conversion
values = [1, 2, 2, 3, 4, 4]
print("set(list)    =", set(values))

# Dictionary Conversion
pairs = [("A", 1), ("B", 2), ("C", 3)]
print("dict(list)   =", dict(pairs))