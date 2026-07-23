# ======================================================
#               PYTHON TUPLE OPERATIONS
# ======================================================

# 1. Creating Tuples
print("\n1. Creating Tuples")

tuple1 = (10, 20, 30, 40, 50)
tuple2 = ("Apple", "Banana", "Mango")

print(tuple1)
print(tuple2)

# ======================================================
# 2. Accessing Elements (Indexing)
# ======================================================

print("\n2. Indexing")

print("First Element :", tuple2[0])
print("Last Element :", tuple2[-1])

# ======================================================
# 3. Slicing
# ======================================================

print("\n3. Slicing")

print(tuple2[0:2])
print(tuple2[:2])
print(tuple2[::-1])

# ======================================================
# 4. Length
# ======================================================

print("\n4. Length")

print(len(tuple2))

# ======================================================
# 5. Concatenation
# ======================================================

print("\n5. Concatenation")

new_tuple = tuple1 + (60, 70)

print(new_tuple)

# ======================================================
# 6. Repetition
# ======================================================

print("\n6. Repetition")

print(tuple2 * 2)

# ======================================================
# 7. Membership Operators
# ======================================================

print("\n7. Membership Operators")

print("Apple" in tuple2)
print("Orange" not in tuple2)

# ======================================================
# 8. Count
# ======================================================

print("\n8. Count")

numbers = (1, 2, 2, 3, 2, 4)

print(numbers.count(2))

# ======================================================
# 9. Index
# ======================================================

print("\n9. Index")

print(numbers.index(3))

# ======================================================
# 10. Maximum, Minimum and Sum
# ======================================================

print("\n10. Max, Min and Sum")

values = (10, 25, 15, 40)

print("Maximum :", max(values))
print("Minimum :", min(values))
print("Sum :", sum(values))

# ======================================================
# 11. Sorting
# ======================================================

print("\n11. Sorting")

print(sorted(values))

# ======================================================
# 12. Nested Tuple
# ======================================================

print("\n12. Nested Tuple")

matrix = ((1, 2), (3, 4))

print(matrix)
print(matrix[1][0])

# ======================================================
# 13. Tuple Packing
# ======================================================

print("\n13. Tuple Packing")

student = ("Rahul", 20, "BCA")

print(student)

# ======================================================
# 14. Tuple Unpacking
# ======================================================

print("\n14. Tuple Unpacking")

name, age, course = student

print(name)
print(age)
print(course)

# ======================================================
# 15. Iterating Through Tuple
# ======================================================

print("\n15. For Loop")

for item in tuple2:
    print(item)

# ======================================================
# 16. Tuple Immutability
# ======================================================

print("\n16. Tuple Immutability")

print("Tuples cannot be changed after creation.")

# tuple2[0] = "Orange"   # This will give an error

# ======================================================
# 17. Convert Tuple to List
# ======================================================

print("\n17. Tuple to List")

temp = list(tuple2)

print(temp)

# ======================================================
# 18. Convert List to Tuple
# ======================================================

print("\n18. List to Tuple")

list1 = [100, 200, 300]

tuple3 = tuple(list1)

print(tuple3)

# ======================================================
# 19. Single Element Tuple
# ======================================================

print("\n19. Single Element Tuple")

single = (5,)

print(single)
print(type(single))

# ======================================================
# 20. Empty Tuple
# ======================================================

print("\n20. Empty Tuple")

empty = ()

print(empty)
print(type(empty))

# ======================================================
# End of Program
# ======================================================

print("\nProgram Completed Successfully!")