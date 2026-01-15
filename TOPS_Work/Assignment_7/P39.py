# 39.	Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().

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


# Output:
# Enter a Number: 4
# Square value of 4.0 is: 2.0
# Ceiling value of 4.0 is: 4
# Floor value of 4.0 is: 4