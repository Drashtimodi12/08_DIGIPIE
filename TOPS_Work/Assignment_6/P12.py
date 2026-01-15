# 12.	Write a Python program to check if a person is eligible to donate blood using a nested if.

# Taking age and weight as input from the user
age = int(input('Enter your age: '))
weight = float(input('Enter your weight: '))

# Check if the person is eligible based on age and weight
if age >= 18 :      # First check: if age is 18 or older
    if weight >= 50 :       # Nested check: if weight is 50 kg or more
        print('You are eligible to donate blood.')
    else :
        print('You must weigh at least 50 kg to donate blood.')
else :
    print('You must be at least 18 years old to donate blood.')