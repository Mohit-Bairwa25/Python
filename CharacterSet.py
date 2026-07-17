import string

# Different character sets available in Python's string module

print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)
print("All letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)
print("Whitespace:", repr(string.whitespace))
print("Printable characters:", string.printable)

# All printable ASCII characters (code 32 to 126)
print("\nASCII printable characters (32-126):")
for code in range(32, 127):
    print(f"{code}: {chr(code)}")