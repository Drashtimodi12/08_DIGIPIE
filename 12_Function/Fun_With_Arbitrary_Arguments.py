# Function with Arbitrary Arguments (*args):- In Python, the *args parameter allows a function to accept a variable 
# number of arguments, which are stored in a tuple. This is useful when you don’t know in advance how many arguments 
# will be passed to the function.

def load(*a) :           # *a collects all arguments into a tuple
    total = 0            # Initialize total sum to 0
    for i in a :         # Iterate through each value in the tuple
        total += i       # Add the value to total
    print(total)         # Print the final sum

# Calling the function with multiple arguments
load(10, 46, 56)

# Output: 112