# Basic String Functions in Python

text = "i am a coder."

print("Original String :", text)

# 1. endswith()
print("\n1. endswith()")
print("Does the string end with 'er.' ? :", text.endswith("er."))
print("Does the string end with 'coder' ? :", text.endswith("coder"))

# 2. capitalize()
print("\n2. capitalize()")
capital_text = text.capitalize()
print("After capitalize() :", capital_text)

# 3. replace()
print("\n3. replace()")
new_text = text.replace("coder", "programmer")
print("After replace() :", new_text)

# 4. find()
print("\n4. find()")
position = text.find("coder")
print("'coder' found at index :", position)

position = text.find("python")
print("'python' found at index :", position)

# 5. count()
print("\n5. count()")
print("'am' occurs", text.count("am"), "time(s)")
print("'a' occurs", text.count("a"), "time(s)")