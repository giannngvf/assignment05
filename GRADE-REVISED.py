print("This program will tell you, your grades' equivalent grade/mark and its description based on the PUP Grading System.")
grade = float(input("Enter your grade: "))
grade1 = round(grade)

if 97 <= grade1 <= 100:
    print("Grade/Mark: 1.0")
    print("Description: Excellent!")
elif 94 <= grade1 <= 96:
    print("Grade/Mark: 1.25")
    print("Description: Excellent!")
elif 91 <= grade1 <= 93:
    print("Grade/Mark: 1.5")
    print("Description: Very Good!")
elif 88 <= grade1 <= 90:
    print("Grade/Mark: 1.75")
    print("Description: Very Good!")
elif 85 <= grade1 <= 87:
    print("Grade/Mark: 2.0")
    print("Description: Good.")
elif 82 <= grade1 <= 84:
    print("Grade/Mark: 2.25")
    print("Description: Good.")
elif 79 <= grade1 <= 81:
    print("Grade/Mark: 2.5")
    print("Description: Satisfactory.")
elif 76 <= grade1 <= 78:
    print("Grade/Mark: 2.75")
    print("Description: Satisfactory.")
elif grade1 == 75:
    print("Grade/Mark: 3.0")
    print("Description: Passing.")
elif 65 <= grade1 <= 74:
    print("Grade/Mark: 5")
    print("Description: Failure.")
else:
    print("Sorry. Your grade isn't considered in the PUP Grading System so we can't tell you its equivalent grade/mark and its description.")