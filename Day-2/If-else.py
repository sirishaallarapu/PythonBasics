#grading system
marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "Fail"
print(f"Your grade is: {grade}")

# Check even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Check the largest
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print(f"The largest number is: {a}")
elif b > c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")

# Check leap year
year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")