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

print("\n--- Student Result ---")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)