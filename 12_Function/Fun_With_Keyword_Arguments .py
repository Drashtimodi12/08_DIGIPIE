# Function with Keyword Arguments (**kwargs):- In Python, **kwargs allows us to pass multiple key-value pairs (like a dictionary) 
# to a function. This makes the function flexible, as we can pass any number of named arguments.
# **a allows passing multiple key-value pairs as a dictionary


# **a collects multiple keyword arguments as a dictionary
def show(**a) :
    print(a)

# Calling the function with keyword arguments
show(python = 10232, java = 40233)

# Output: {'python': 10232, 'java': 40233}