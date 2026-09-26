marks1 = int(input("Enter marks of Subject 1: "))
marks2 = int(input("Enter marks of Subject 2: "))
marks3 = int(input("Enter marks of Subject 3: "))

if marks1 >= 20 and marks2 >= 20 and marks3 >= 20:
    print("\nResult: PASS")
else:
    print("\nResult: FAIL")

if marks1 < 20:
    print("Subject 1: FAIL")

if marks2 < 20:
    print("Subject 2: FAIL")

if marks3 < 20:
    print("Subject 3: FAIL")