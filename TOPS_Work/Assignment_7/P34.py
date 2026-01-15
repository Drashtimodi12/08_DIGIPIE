# 34.	Write a Python program to create a calculator using functions.

# Define functions for basic arithmetic operations
def add(x, y) :
    return x + y

def subtract(x ,y) :
    return x - y

def multiply(x ,y) :
    return x * y

def divide(x, y) :
    if y == 0 :
        return "Error! Division By ZERO."
    return x / y

# Main program to use the calculator functions
def calculator() :
    print("---SELECT OPERATION---")
    print("1. Addition")
    print("2. Subteact")
    print("3. Multiply")
    print("4. Divide")

    while True :
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if the choice is one of the four options
        if choice in ["1", "2", "3", "4"] :
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1" :
                print(f"The ADITION of {num1} and {num2} is: {add(num1, num2)}.")

            elif choice == "2" :
                print(f"The SUBTRACT of {num1} and {num2} is: {subtract(num1, num2)}.")

            elif choice == "3" :
                print(f"The MUTIPLICATION of {num1} and {num2} is: {multiply(num1, num2)}.")

            elif choice == "4" :
                print(f"The DIVIDE of {num1} and {num2} is: {divide(num1, num2)}")

        else :
            print("Invalid Input.")

        # Ask if the user wants to perform another calculation
        C_continue = input("Do you want to perform another calculation? (yes/no): ")

        if C_continue.lower() != "yes" :
            break

# Run the calculator function
calculator()