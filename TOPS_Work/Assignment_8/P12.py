# 12.	Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input). 

def calculator() :
    try :
        # Taking user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+" :
            result = num1 + num2
        elif operation == "-" :
            result = num1 - num2
        elif operation == "*" :
            result = num1 * num2
        elif operation == "/" :
            if num2 == 0 :
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
                result = num1 / num2
            else :
                raise ValueError("Error: Invalid operation! Please use +, -, *, or /.")
            
            print(f"Result: {result}")


    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
calculator()



# Output:
# Enter first number: 2
# Enter second number: 0
# Enter operation (+, -, *, /): /
# Error: Division by zero is not allowed.