# 7.	How to take user input using the input() function.

# By default, input() returns a string. 
# If you need other types (integer, float, etc.), you must convert them using int(), float(), or bool().

# Taking string input
name = input('Enter your name: ')
print('Hello!', name, 'Welcome!')

# Convert input to integer
age = int(input('Enter your age: '))
print('Your age is: ', age)

# Convert input to float
height = float(input('Enter your height: '))
print('Your height is: ', height, 'Meters')

# You can take multiple inputs in a single line using split().
name, age = input('Enter your name and age (separated by space): ').split()
print('Name:', name)
print('Age:', age)

# Use map() to convert multiple inputs into integers or floats.
a, b, c = map(int, input('Enter three numbers: ').split())
print('Sum:', a + b + c) 