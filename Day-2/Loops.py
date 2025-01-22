#Sum of numbers using for loop
N = 10
sum_of_numbers = 0
for i in range(1, N+1):
    sum_of_numbers += i
print(f"Sum of first {N} numbers: {sum_of_numbers}")

#Sum of numbers using while loop
N = 10
sum_of_numbers = 0
i = 1
while i <= N:
    sum_of_numbers += i
    i += 1
print(f"Sum of first {N} numbers: {sum_of_numbers}")

# Factorial using for loop
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

#Factorial using while loop
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num}: {factorial}")

#Create a pattern using for loop
rows = 5
for i in range(1, rows + 1):
    print("*" *i)
    
#Create a pattern using while loop
rows = 5
i = 1
while i <= rows:
    print("*" * i)
    i += 1