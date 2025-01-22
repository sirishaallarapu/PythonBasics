#Functions
#Prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

number = int(input("enter number"))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Factorial
def factorial_for(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("enter number"))
print(f"Factorial of {number} using for loop is: {factorial_for(number)}")