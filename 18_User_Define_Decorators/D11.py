# Define a decorator function named 'multiply'
def multiply(func) :
    def wrap(*a) :      # Wrapper function that accepts any number of arguments
        multiply = 1    # Initialize multiplication result to 1

        # Loop through all arguments and multiply them
        for i in a :
            multiply *= i

        print("Multiplication is: ", multiply)      # Print the multiplication result

        func(*a)            # Call the original function

    return wrap     # Return the wrapper function



# Apply the 'multiply' decorator to the 'result' function
@multiply
def result(a, b) :
    print("Multiply Calling...")        # This function just prints a message

result(10, 20)      # Call the decorated function

# Output:
# Multiplication is:  200
# Multiply Calling...