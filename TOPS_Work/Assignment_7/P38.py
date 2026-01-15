# 38.	Write a Python program to create a lambda function with two expressions.

# Create a lambda function that performs two operations (calculates the sum and product of two numbers)
operations = lambda x , y : (x + y, x * y)

# Take two numbers from the user
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

# Calculate the sum and product using the lambda function
sum, mul = operations(num1, num2)

# Print the results
print(f"Sum of {num1} and {num2} is: {sum}")
print(f"Multiplication of {num1} and {num2} is: {mul}")

# Output:
# Enter first num: 3
# Enter second num: 6
# Sum of 3.0 and 6.0 is: 9.0
# Multiplication of 3.0 and 6.0 is: 18.0