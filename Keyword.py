# import, from, as
import math as m
from math import sqrt

# True, False, None
flag = True
status = False
value = None

# global
x = 100

def global_demo():
    global x
    x = 200

global_demo()

# class, pass
class Student:
    pass

# def, return
def add(a, b):
    return a + b

print("Addition:", add(5, 7))

# lambda
square = lambda n: n * n
print("Square:", square(5))

# yield
def generator():
    yield 1
    yield 2

for num in generator():
    print("Yield:", num)

# nonlocal
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner()

print("Nonlocal:", outer())

# assert
assert add(2, 3) == 5

# if, elif, else
age = 20

if age > 18:
    print("Adult")
elif age == 18:
    print("Exactly 18")
else:
    print("Minor")

# and, or, not
a = 5
b = 10

if a < b and not (a > b):
    print("Logical operators work")

if a == 5 or b == 5:
    print("OR works")

# for, in, continue, break
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("For:", i)

# while
count = 0
while count < 2:
    print("While:", count)
    count += 1

# is
c = value
print("Identity:", c is None)

# del
temp = 50
del temp

# with, as
with open("sample.txt", "w") as file:
    file.write("Hello Python")

# try, except, finally, raise
try:
    raise ValueError("Example Error")
except ValueError as e:
    print("Caught:", e)
finally:
    print("Finally block executed")

# match, case
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# async, await
async def async_demo():
    return "Hello Async"

# await async_demo()      # Only valid inside another async function.

print("Square root:", sqrt(49))
print("Pi:", m.pi)