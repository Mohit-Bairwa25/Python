# Program to demonstrate all Logical Operators in Python

# Input two numbers
a = 20
b = 10

print("First Number (a):", a)
print("Second Number (b):", b)

# Using AND Operator
if a > b and b > 0:
    print("\nAND Operator: Both conditions are True")

# Using OR Operator
if a < b or a > 15:
    print("OR Operator: At least one condition is True")

# Using NOT Operator
if not (a < b):
    print("NOT Operator: The condition (a < b) is False, so NOT makes it True")