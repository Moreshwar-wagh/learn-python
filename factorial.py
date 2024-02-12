# Factorial in python using library function

import math

# Using Factorial Function in Python Factorial Program.
# num = int(input("Enter a number: "))
num = 5
factorial = math.factorial(num)
print("Factorial of", num, "is", factorial)

# For Loop
num = 5
factorial = 1
if num >= 1:
    for i in range(1, num + 1):
        factorial = factorial * i
print("The factorial of", num, "is", factorial)


# Using Recursion in Python Factorial program.
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = 5
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
