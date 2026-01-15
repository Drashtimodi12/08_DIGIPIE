# Define a decorator function named 'before'
def before(func) :

    # Define an inner function 'wrap' that will wrap the original function
    def wrap() :
        # Print a message before calling the original function
        print(f"Print BEFORE something....{func.__name__}")
        # Call the original function
        func()
        # Print a message after calling the original function
        print("AFTER somethnig...")
    # Return the inner function 'wrap' as the decorated function
    return wrap

# Use the 'before' decorator to modify the 'test' function
@before
def test() :
    # Print a message indicating that the 'test' function is being called
    print("Printing something...")

# Use the 'before' decorator to modify the 'disp' function
@before
def disp() :
    # Print a message indicating that the 'disp' function is being called
    print("Display calling...")


test()      # Call the decorated 'test' function
# Output:
# Print BEFORE something....test
# Printing something...
# AFTER somethnig...


disp()      # Call the decorated 'disp' function
# Output:
# Print BEFORE something....disp
# Display calling...
# AFTER somethnig...