print("===================================")
print("   STUDENT RESULT MANAGEMENT SYSTEM")
print("===================================")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")

print("\nEnter marks out of 50")

marks1 = int(input("Enter marks of Subject 1: "))
marks2 = int(input("Enter marks of Subject 2: "))
marks3 = int(input("Enter marks of Subject 3: "))

total = marks1 + marks2 + marks3
percentage = (total / 150) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if marks1 >= 20 and marks2 >= 20 and marks3 >= 20:
    result = "PASS"
else:
    result = "FAIL"

print("\n===================================")
print("           STUDENT RESULT")
print("===================================")
print("Name       :", name)
print("Roll Number:", roll_no)
print("Branch     :", branch)
print("Total Marks:", total, "/ 150")
print("Percentage :", percentage, "%")
print("Grade      :", grade)
print("Result     :", result)
print("===================================")
