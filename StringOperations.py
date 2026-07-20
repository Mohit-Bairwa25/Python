# ======================================================
#           PYTHON STRING OPERATIONS
# ======================================================

# Creating Strings
str1 = "Hello"
str2 = "Python"

print("String 1 :", str1)
print("String 2 :", str2)

# ======================================================
# 1. Concatenation (+)
# ======================================================
print("\n1. Concatenation")
print(str1 + " " + str2)

# ======================================================
# 2. Repetition (*)
# ======================================================
print("\n2. Repetition")
print(str1 * 3)

# ======================================================
# 3. Indexing
# ======================================================
print("\n3. Indexing")
print("First Character :", str1[0])
print("Last Character :", str1[-1])

# ======================================================
# 4. Slicing
# ======================================================
print("\n4. Slicing")
print("First 3 Characters :", str1[:3])
print("Last 3 Characters :", str1[-3:])
print("Middle Characters :", str1[1:4])
print("Reverse String :", str1[::-1])

# ======================================================
# 5. Length
# ======================================================
print("\n5. Length")
print(len(str1))

# ======================================================
# 6. Membership Operators
# ======================================================
print("\n6. Membership Operators")
print("Hel" in str1)
print("abc" not in str1)

# ======================================================
# 7. Case Conversion
# ======================================================
print("\n7. Case Conversion")

text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# ======================================================
# 8. Removing Spaces
# ======================================================
print("\n8. Strip Functions")

name = "   Mohit   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

# ======================================================
# 9. Find and Index
# ======================================================
print("\n9. Find and Index")

sentence = "Python Programming"

print(sentence.find("Pro"))
print(sentence.index("Pro"))

# ======================================================
# 10. Replace
# ======================================================
print("\n10. Replace")

print(sentence.replace("Programming", "Language"))

# ======================================================
# 11. Count
# ======================================================
print("\n11. Count")

print(sentence.count("m"))

# ======================================================
# 12. Startswith and Endswith
# ======================================================
print("\n12. Startswith & Endswith")

print(sentence.startswith("Python"))
print(sentence.endswith("ing"))

# ======================================================
# 13. Split
# ======================================================
print("\n13. Split")

words = sentence.split()

print(words)

# ======================================================
# 14. Join
# ======================================================
print("\n14. Join")

new_string = "-".join(words)

print(new_string)

# ======================================================
# 15. Comparison
# ======================================================
print("\n15. String Comparison")

print("apple" == "apple")
print("apple" != "Apple")
print("apple" > "banana")
print("cat" < "dog")

# ======================================================
# 16. Checking Functions
# ======================================================
print("\n16. Checking Functions")

print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print(" ".isspace())
print("Hello".istitle())

# ======================================================
# 17. Escape Characters
# ======================================================
print("\n17. Escape Characters")

print("Hello\nPython")
print("Hello\tPython")
print("Hello\\Python")
print("He said \"Hello\"")

# ======================================================
# 18. Formatting
# ======================================================
print("\n18. String Formatting")

name = "Mohit"
age = 29

print("My name is {} and I am {} years old.".format(name, age))

print(f"My name is {name} and I am {age} years old.")

# ======================================================
# 19. ASCII Conversion
# ======================================================
print("\n19. ASCII Conversion")

print(ord('A'))
print(chr(65))

# ======================================================
# 20. Center, Left Justify, Right Justify
# ======================================================
print("\n20. Alignment")

print(str1.center(20, '-'))
print(str1.ljust(20, '-'))
print(str1.rjust(20, '-'))

# ======================================================
# 21. Zero Fill
# ======================================================
print("\n21. Zero Fill")

print("25".zfill(5))

# ======================================================
# 22. Partition
# ======================================================
print("\n22. Partition")

print(sentence.partition(" "))

# ======================================================
# 23. Encode
# ======================================================
print("\n23. Encode")

print(str1.encode())

# ======================================================
# 24. String Multiplication and Addition
# ======================================================
print("\n24. Combined Operations")

print((str1 + " ") * 3)

# ======================================================
# 25. Raw String
# ======================================================
print("\n25. Raw String")

print(r"C:\Users\Mohit\Documents")

# ======================================================
# End of Program
# ======================================================
print("\nProgram Completed Successfully!")