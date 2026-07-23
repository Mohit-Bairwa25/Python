# ======================================================
#               PYTHON LIST OPERATIONS
# ======================================================

# 1. Creating a List
print("\n1. Creating a List")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

# ======================================================
# 2. Indexing
# ======================================================

print("\n2. Indexing")

print("First Element :", fruits[0])
print("Last Element :", fruits[-1])

# ======================================================
# 3. Slicing
# ======================================================

print("\n3. Slicing")

print(fruits[1:3])
print(fruits[:2])
print(fruits[::-1])

# ======================================================
# 4. Length
# ======================================================

print("\n4. Length")

print(len(fruits))

# ======================================================
# 5. Adding Elements
# ======================================================

print("\n5. Adding Elements")

fruits.append("Grapes")
print("append():", fruits)

fruits.insert(1, "Pineapple")
print("insert():", fruits)

# ======================================================
# 6. Extending List
# ======================================================

print("\n6. Extending List")

fruits.extend(["Kiwi", "Papaya"])
print(fruits)

# ======================================================
# 7. Removing Elements
# ======================================================

print("\n7. Removing Elements")

fruits.remove("Banana")
print("remove():", fruits)

fruits.pop()
print("pop():", fruits)

del fruits[1]
print("del:", fruits)

# ======================================================
# 8. Updating Elements
# ======================================================

print("\n8. Updating Elements")

fruits[0] = "Cherry"
print(fruits)

# ======================================================
# 9. Membership Operators
# ======================================================

print("\n9. Membership Operators")

print("Mango" in fruits)
print("Apple" not in fruits)

# ======================================================
# 10. Sorting
# ======================================================

print("\n10. Sorting")

numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# ======================================================
# 11. Reverse
# ======================================================

print("\n11. Reverse")

numbers.reverse()
print(numbers)

# ======================================================
# 12. Count
# ======================================================

print("\n12. Count")

nums = [1, 2, 2, 3, 2, 4]

print(nums.count(2))

# ======================================================
# 13. Index
# ======================================================

print("\n13. Index")

print(nums.index(3))

# ======================================================
# 14. Copy
# ======================================================

print("\n14. Copy")

new_list = nums.copy()

print(new_list)

# ======================================================
# 15. Clear
# ======================================================

print("\n15. Clear")

temp = [10, 20, 30]

temp.clear()

print(temp)

# ======================================================
# 16. Concatenation
# ======================================================

print("\n16. Concatenation")

list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)

# ======================================================
# 17. Repetition
# ======================================================

print("\n17. Repetition")

print(list1 * 3)

# ======================================================
# 18. Nested List
# ======================================================

print("\n18. Nested List")

matrix = [[1, 2], [3, 4]]

print(matrix)
print(matrix[0][1])

# ======================================================
# 19. List Comprehension
# ======================================================

print("\n19. List Comprehension")

square = [x*x for x in range(1, 6)]

print(square)

# ======================================================
# 20. Maximum and Minimum
# ======================================================

print("\n20. Max and Min")

print(max(numbers))
print(min(numbers))

# ======================================================
# 21. Sum
# ======================================================

print("\n21. Sum")

print(sum(numbers))

# ======================================================
# 22. Iterating Through List
# ======================================================

print("\n22. For Loop")

for item in fruits:
    print(item)

# ======================================================
# End of Program
# ======================================================

print("\nProgram Completed Successfully!")