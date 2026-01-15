# Create a menu-driven calculator (Add, Subtract, Multiply, Divide) using user-defined functions.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Divide with 0 is not possible"
    else:
        return a / b
    
while True:
    print("----SEELECT OPERATION----")
    print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. divide \n 5. Exit")
    c = int(input("Enter opertion from 1 to 5: "))
    
    
    if c == 5:
        print("Thank you for Visiting.")
        break
        
    d = float(input("Enter first number: "))
    e = float(input("Enter second number: "))

    if c == 1:
        print(add(d, e))
    elif c == 2:
        print(sub(d, e))
    elif c == 3:
        print(mul(d, e))
    elif c == 4:
        print(div(d, e))
    elif c == 5:
        print(div(d, e))
    else:
        print("Invalid choice! Please try again.")


# OP:
# ----SEELECT OPERATION----
#  1. Addition 
#  2. Subtraction
#  3. Multiplication
#  4. divide
#  5. Exit
# Enter opertion from 1 to 5: 1
# Enter first number: 2
# Enter second number: 3
# 5.0
# ----SEELECT OPERATION----
#  1. Addition
#  2. Subtraction
#  3. Multiplication
#  4. divide
#  5. Exit
# Enter opertion from 1 to 5: 3
# Enter first number: 2
# Enter second number: 2
# 4.0
# ----SEELECT OPERATION----
#  1. Addition
#  2. Subtraction
#  3. Multiplication
#  4. divide
#  5. Exit
# Enter opertion from 1 to 5: 5
# Thank you for Visiting.