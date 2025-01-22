#Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

#Transform Data (Square of Numbers)
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("Squared numbers:", squared_numbers)

#Filter Even Numbers and Transform (Square them)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Squares of even numbers:", even_squares)

# List comprehension to transform strings to uppercase
words = ["apple", "banana", "cherry", "date"]
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)


#Extracting Values from a List of Dictionaries

students = [
    {'name': 'Nani', 'age': 25, 'grade': 'A'},
    {'name': 'Siri', 'age': 22, 'grade': 'B'},
    {'name': 'Lishi', 'age': 23, 'grade': 'A'},
    {'name': 'Ruby', 'age': 24, 'grade': 'C'}
]

names = [student['name'] for student in students]

grades_A = [student['grade'] for student in students if student['grade'] == 'A']

print("Names of all students:", names)
print("Students with grade 'A':", grades_A)

name_age = [(student['name'], student['age']) for student in students]
print("Names and Ages of students:", name_age)