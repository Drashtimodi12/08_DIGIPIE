# 40.	Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

# Taking three integer inputs from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Checking if any two numbers are equal
if a == b or b == c or a == c :
    result = 0
else :
    result = a + b + c

# Printing the result
print(f'Result of Sum: {result}')