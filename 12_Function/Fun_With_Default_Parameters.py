# Function with Default Parameters:- It allow a function to have pre-defined values, which are used if no argument 
# is provided during the function call.
# A function with default values.

# Default values are assigned to parameters
def stu(a =10, b = "Drashti") :
    print(a, b)

# Calling the function without any arguments
stu()               # Output: 10 Drashti

# Calling the function with both arguments
stu(3, "Modi")      # Output: 3 Modi

# Calling the function with only one argument (keyword argument)
stu(b = "Python")   # Output: 10 Python