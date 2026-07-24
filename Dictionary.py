# ======================================================
#             PYTHON DICTIONARY OPERATIONS
# ======================================================

# 1. Creating a Dictionary
print("\n1. Creating a Dictionary")

student = {
    "Name": "Neeraj",
    "Age": 20,
    "Course": "BCA"
}

print(student)

# ======================================================
# 2. Accessing Values
# ======================================================

print("\n2. Accessing Values")

print(student["Name"])
print(student.get("Course"))

# ======================================================
# 3. Length
# ======================================================

print("\n3. Length")

print(len(student))

# ======================================================
# 4. Adding New Item
# ======================================================

print("\n4. Adding New Item")

student["City"] = "Jaipur"

print(student)

# ======================================================
# 5. Updating Values
# ======================================================

print("\n5. Updating Values")

student.update({
    "Age": 21,
    "Course": "BTech"
})

print(student)

# ======================================================
# 6. Removing Items
# ======================================================

print("\n6. Removing Items")

student.pop("City")
print("After pop():", student)

student["State"] = "Rajasthan"

del student["State"]
print("After del:", student)

# ======================================================
# 7. Membership Operators
# ======================================================

print("\n7. Membership Operators")

print("Name" in student)
print("Phone" not in student)

# ======================================================
# 8. Dictionary Keys
# ======================================================

print("\n8. Keys")

print(student.keys())

# ======================================================
# 9. Dictionary Values
# ======================================================

print("\n9. Values")

print(student.values())

# ======================================================
# 10. Dictionary Items
# ======================================================

print("\n10. Items")

print(student.items())

# ======================================================
# 11. Copy Dictionary
# ======================================================

print("\n11. Copy")

new_student = student.copy()

print(new_student)

# ======================================================
# 12. Update Dictionary
# ======================================================

print("\n12. Update")

student.update({"Marks":95})

print(student)

# ======================================================
# 13. Loop Through Dictionary
# ======================================================

print("\n13. Loop Through Dictionary")

for key in student:
    print(key, ":", student[key])

# ======================================================
# 14. Loop Using items()
# ======================================================

print("\n14. Loop Using items()")

for key, value in student.items():
    print(key, ":", value)

# ======================================================
# 15. Nested Dictionary
# ======================================================

print("\n15. Nested Dictionary")

students = {
    "Student1":{
        "Name":"Naina",
        "Age":20
    },
    "Student2":{
        "Name":"Amit",
        "Age":21
    }
}

print(students)

print(students["Student1"]["Name"])

# ======================================================
# 16. Dictionary Comprehension
# ======================================================

print("\n16. Dictionary Comprehension")

square = {x:x*x for x in range(1,6)}

print(square)

# ======================================================
# 17. popitem()
# ======================================================

print("\n17. popitem()")

data = {
    "A":1,
    "B":2,
    "C":3
}

print(data.popitem())

print(data)

# ======================================================
# 18. setdefault()
# ======================================================

print("\n18. setdefault()")

student.setdefault("City","Delhi")

print(student)

# ======================================================
# 19. fromkeys()
# ======================================================

print("\n19. fromkeys()")

keys = ("Name","Age","Course")

new_dict = dict.fromkeys(keys,"Not Available")

print(new_dict)

# ======================================================
# 20. Clear Dictionary
# ======================================================

print("\n20. Clear")

temp = {
    "A":10,
    "B":20
}

temp.clear()

print(temp)

# ======================================================
# 21. Empty Dictionary
# ======================================================

print("\n21. Empty Dictionary")

empty = {}

print(empty)

# ======================================================
# 22. Dictionary with Different Data Types
# ======================================================

print("\n22. Different Data Types")

info = {
    "Name":"Aditi",
    "Age":20,
    "Marks":89.5,
    "Passed":True,
    "Subjects":["Python","Math"]
}

print(info)

# ======================================================
# 23. Dictionary is Mutable
# ======================================================

print("\n23. Mutable Property")

student["Course"] = "MCA"

print(student)

# ======================================================
# End of Program
# ======================================================

print("\nProgram Completed Successfully!")