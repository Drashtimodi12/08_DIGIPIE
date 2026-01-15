# Define a decorator function named 'add'
def add(func) :
    def wrap(*a) :      # Wrapper function that accepts any number of arguments
        sum = 0    # Initialize sum result to 0

        # Loop through all arguments and sum them
        for i in a :
            sum += i

        print("Addition is: ", sum)      # Print the Addition result

        func(*a)            # Call the original function

    return wrap     # Return the wrapper function



# Apply the 'add' decorator to the 'result' function
@add
def result(a, b) :
    print("Addition Calling...")        # This function just prints a message

result(10, 20)      # Call the decorated function

# Output:
# Addition is:  30
# Addition Calling...