# 37.	Write a Python program to create a lambda function with one expression. 

# Create a lambda function with one expression to calculate the square of a number
square = lambda a : a * a


# Take a number from the user
num = float(input("Enter a number: "))

# Calculate the square using the lambda function
result = square(num)

# Print the result
print(f"Square of {num} is:  {result}")


# Output:
# Enter a number: 4
# Square of 4.0 is:  16.0