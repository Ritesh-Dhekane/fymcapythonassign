# 24. Python program to check student loan eligibility

print("Name = Ritesh Dhekane")

# Take input from user
student_name = input("Enter student's name: ")
age = int(input("Enter age: "))
marks = float(input("Enter academic percentage: "))

# Check eligibility
if 17 <= age <= 21 and marks >= 80:
    print(f"{student_name} is eligible for the student loan.")
else:
    print(f"{student_name} is not eligible for the student loan.")
