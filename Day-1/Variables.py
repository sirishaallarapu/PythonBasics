name = "Sirisha"
age = 23
subjects = ["Math", "English", "Physics", "Chemistry"]

print(type(name))

print(type(age))

print(type(subjects))

#expressions
pi = 3.1416
radius = 10
perimeter = 2 * pi * radius
print(perimeter)

#object counters
str_counter = 0

for item in ("Sirisha", 23, "Data Engineer", None, True, "Infoobjects"):
    if isinstance(item, str):
         str_counter += 1

print(str_counter)

#Accumulators
numbers = [1, 2, 3, 4]
total=0

for n in numbers:
    total += n
print(total)

#Temporary variables
a = 1
b = 5

temp = a
a = b
b = temp

print(a)
print(b)

#loop variables
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]
for color in colors:
    print(color)

for index, color in enumerate(colors):
    print(index, color)

#data storage variables
employees=[ ("Alice" , "alice@gmail.com" , "101"), ("Bob" , "bob@gmail.com" , "102"), ("Cherry" , "cherry@gmail.com" , "103")]
for canditate in employees:
    print(canditate)
for name, email, id in employees:
    print(id, name)

#variables having dynamic types
value = "A string value"
print(value.upper())
print(value.lower())

#Class and instance variables
class Employee:
    count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")







