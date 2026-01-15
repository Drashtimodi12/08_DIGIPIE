# 41.	Write a Python program to demonstrate the use of functions from the math module. 

# Import the math module
import math

num = float(input("Enter a Number: "))

# Calculate the square root of the number
square = math.sqrt(num)
print(f"Square value of {num} is: {square}")

# Calculate the ceiling value of the number
ceil = math.ceil(num)
print(f"Ceiling value of {num} is: {ceil}")

# Calculate the floor value of the number
floor = math.floor(num)
print(f"Floor value of {num} is: {floor}")

# Calculate the factorial of a number
factorial = math.factorial(5)
print(f"Factorial value of 5 is: {factorial}")

# Calculate the sine of a number (in radians)
sin = math.sin(math.radians(30))
print(f"The sine of 30 degrees is: {sin}")

# Calculate the logarithm of a number to base 10
log = math.log10(100)
print(f"The base-10 algorithm of 100 is: {log}")


# Output: 
# Enter a Number: 16
# Square value of 16.0 is: 4.0
# Ceiling value of 16.0 is: 16
# Floor value of 16.0 is: 16
# Factorial value of 5 is: 120
# The sine of 30 degrees is: 0.49999999999999994
# The base-10 algorithm of 100 is: 2.0