# 15.	Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 

def handle_exception() :

    try :
        # Trying to open a file that does not exist
        with open("P10.txt", "r") as file :
            content = file.read()

        # Trying to divide by zero
        result = 10 / 0
        print(f"Result of Division: {result}")

    except FileNotFoundError as e :
        print(e)

    except ZeroDivisionError as z :
        print(z)

    except Exception as ex :
        print(ex)

# Call the function to demonstrate exception handling
handle_exception()

# Output:
# [Errno 2] No such file or directory: 'P10.txt'