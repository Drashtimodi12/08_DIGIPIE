# 38.	Write python program that swap two number with temp variable and without temp variable. 

# Using a temporary variable
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

print(f'Before Swapping a = {a}, and b = {b}.')

# Swap using temp variable
temp = a
a = b
b = temp

print(f'After Swapping a = {a}, and b = {b}.')



# Without using a temporary variable
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Before swapping: x = {x}, y = {y}")

# Swap without temp variable
x, y = y, x  # Tuple unpacking

print(f"After swapping: x = {x}, y = {y}")