# Program to demonstrate Type Casting in Python

# -------------------------------
# Implicit Type Casting
# -------------------------------

print("----- Implicit Type Casting -----")

a = 10          # Integer
b = 5.5         # Float

c = a + b       # int is automatically converted to float

print("a =", a)
print("b =", b)
print("a + b =", c)
print("Data Type of c:", type(c))


# -------------------------------
# Explicit Type Casting
# -------------------------------

print("\n----- Explicit Type Casting -----")

# Integer
num = 25

# Float
decimal = 15.75

# String
text = "100"

# Boolean
flag = True

# int()
print("int(decimal) =", int(decimal))

# float()
print("float(num) =", float(num))

# str()
print("str(num) =", str(num))

# bool()
print("bool(num) =", bool(num))

# complex()
print("complex(num) =", complex(num))

# list()
t = (1, 2, 3)
print("list(tuple) =", list(t))

# tuple()
l = [4, 5, 6]
print("tuple(list) =", tuple(l))

# set()
l2 = [1, 2, 2, 3, 3]
print("set(list) =", set(l2))

# dict()
pairs = [("Name", "Mohit"), ("Age", 29)]
print("dict(list) =", dict(pairs))