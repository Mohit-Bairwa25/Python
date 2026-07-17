# identifiers.py
# Rules for Identifiers in Python
# 1. Can contain letters, digits, and underscores
# 2. Cannot start with a digit
# 3. Cannot contain spaces or special symbols (@, #, %, etc.)
# 4. Cannot be a Python reserved keyword
# 5. Are case-sensitive (age, Age, and AGE are all different)

# ---- Valid identifiers ----
student_name = "Mohit"
_age = 25
marks2 = 90
totalMarks = 100

print("Valid identifiers:")
print("student_name =", student_name)
print("_age =", _age)
print("marks2 =", marks2)
print("totalMarks =", totalMarks)

# ---- Case sensitivity example ----
value = 10
Value = 20
VALUE = 30
print("\nCase sensitivity:")
print("value =", value, ", Value =", Value, ", VALUE =", VALUE)

# ---- Checking if a string is a valid identifier ----
test_names = ["student_name", "2marks", "total marks", "class", "_hidden", "totalMarks"]

print("\nChecking identifier validity:")
for name in test_names:
    print(f"{name!r}: valid = {name.isidentifier()}")

# Note: isidentifier() checks syntax rules but not whether
# the name is a reserved keyword. Use keyword.iskeyword() for that.
import keyword
print("\nChecking against Python keywords:")
for name in test_names:
    if name.isidentifier() and keyword.iskeyword(name):
        print(f"{name!r} is a valid identifier format but is a reserved keyword")