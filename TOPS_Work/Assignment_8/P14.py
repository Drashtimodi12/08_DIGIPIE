# 14.	Write a Python program to handle exceptions in a calculator. 

def add(a, b) :
    return a + b 

def sub(a, b) :
    return a - b

def mul(a, b) :
    return a * b 

def divide(a, b) :
    if b == 0 :
        raise ZeroDivisionError("division by zero is not allowed")
    return a / b

def calculator() :
    try:

        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /):")

        # Perform the appropriate operation
        if operation == "+" :
            result = add(num1, num2)
        elif operation == "-" :
            result = sub(num1, num2)
        elif operation == "*" :
            result = mul(num1, num2)
        elif operation == "/" :
            result = divide(num1, num2)
        else:
            raise ValueError("Invalid operation")
        
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ZeroDivisionError as z :
        print(z)
    except ValueError as v :
        print(v)
    except Exception as ex :
        print(ex)
    
# Run the calculator function
if __name__ == "__main__" :
    calculator()