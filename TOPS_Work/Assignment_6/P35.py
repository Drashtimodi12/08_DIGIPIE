# 35.	Write a Python program to check if a number is positive, negative or zero. 

# Take input from the user
num = float(input('Enter any number: '))

# Check the condition
if num > 0 :
    print(f'Enter {num} is Positive.')
elif num < 0 :
    print(f'Enter {num} is Negative.')
else :
    print(f'Enter {num} is Zero.')