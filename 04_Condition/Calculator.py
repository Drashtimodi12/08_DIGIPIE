# Simple Calculator Program

# Taking user input
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Displaying operation choices
print('---Select Operator---')
print('1. Addition (+)')
print('2. Subtraction (-)')
print('3. Multiplication (*)')
print('4. Division (/)')
print('5. Modulus (%)')
print('6. Exit')

# Taking user choice
choice = int(input('Enter choice (1/2/3/4/5/6): '))

# Performing basic operations
if choice == 1:
    print("Addition:", num1 + num2)
elif choice == 2:
    print("Subtraction:", num1 - num2)
elif choice == 3:
    print("Multiplication:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")
elif choice == 5:
    if num2 != 0:
        print("Modulus:", num1 % num2)
    else:
        print("Error! Cannot divide by zero.")
elif choice == 6:
    print("Exit the calculator.")
else:
    print("Invalid choice! Please enter a valid option.")

# OP:
# Enter first number: 3
# Enter second number: 2
# ---Select Operator---
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Modulus (%)
# 6. Exit
# Enter choice (1/2/3/4/5/6): 2
# Subtraction: 1.0