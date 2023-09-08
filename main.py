def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input a number
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))