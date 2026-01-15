# Check Odd, Even, or Zero
# Write a program to take a number from the user and check:

num = float(input("Enter any number: "))

if num == 0:
    print("Number is zero.")
elif num % 2 == 0:
    print("Number is Even.")
else:
    print("Nmber is Odd.")
# OP:
# Enter any number: 3
# Nmber is Odd.