# 9.	Write a Python program to find greater and less than a number using if_else.

# Taking input from the user
a, b = map(int, input('Enter two numbers: ').split())

# Checking which number is greater
if a > b :
    print(a, 'is greater than', b,'.')
else :
    print(a, 'is less than', b,'.')