# Nested if-elif-else Example

marks = 82

if marks >= 50:
    print("You have passed.")

    if marks >= 90:
        print("Grade: A")

    elif marks >= 75:
        print("Grade: B")

    elif marks >= 60:
        print("Grade: C")

    else:
        print("Grade: D")

else:
    print("You have failed.")