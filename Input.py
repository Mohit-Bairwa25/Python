# Program to demonstrate different types of user input in Python

# -------------------------------
# String Input
# -------------------------------
name = input("Enter your name: ")

# -------------------------------
# Integer Input
# -------------------------------
age = int(input("Enter your age: "))

# -------------------------------
# Float Input
# -------------------------------
salary = float(input("Enter your salary: "))

# -------------------------------
# Boolean Input
# -------------------------------
choice = input("Are you a student? (True/False): ")
student = choice == "True"

# -------------------------------
# Complex Number Input
# -------------------------------
number = complex(input("Enter a complex number (e.g. 3+4j): "))

# -------------------------------
# Multiple Integer Inputs
# -------------------------------
a, b = map(int, input("Enter two integers separated by space: ").split())

# -------------------------------
# Multiple Float Inputs
# -------------------------------
x, y = map(float, input("Enter two decimal numbers separated by space: ").split())

# -------------------------------
# List Input
# -------------------------------
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# -------------------------------
# Tuple Input
# -------------------------------
t = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# -------------------------------
# Set Input
# -------------------------------
s = set(map(int, input("Enter set elements separated by space: ").split()))

# -------------------------------
# Display Output
# -------------------------------
print("\n---------- OUTPUT ----------")

print("Name :", name)
print("Age :", age)
print("Salary :", salary)
print("Student :", student)
print("Complex Number :", number)
print("Two Integers :", a, b)
print("Two Floats :", x, y)
print("List :", numbers)
print("Tuple :", t)
print("Set :", s)

"""
Enter your name: Mohit
Enter your age: 29
Enter your salary: 35000.50
Are you a student? (True/False): False
Enter a complex number (e.g. 3+4j): 2+5j
Enter two integers separated by space: 10 20
Enter two decimal numbers separated by space: 5.5 6.8
Enter list elements separated by space: 1 2 3 4 5
Enter tuple elements separated by space: 6 7 8 9
Enter set elements separated by space: 10 20 20 30
"""