"""
1. Function Decorator (Basic Decorator):-  This is the most common type.
    Wraps a function
    Adds extra behavior
    Uses *args and **kwargs
"""

# Decorator function
def greet(fx):
    # Inner function that will wrap the original function
    def mfx(*arge, **kwargs):
        print("Good Morning!")              # Code before calling actual function
        fx(*arge, **kwargs)                 # Calling the original function
        print("Thanks for using Function...\n")    # Code after calling the function
    return mfx                               # Returning the modified function

# Applying the greet decorator to hello()
@greet
def hello():
    print("Hello World")                     # Original function

# Applying the greet decorator to add()
@greet
def add(a, b):
    print(a + b)                              # Function that prints the sum

# Calling decorated hello()
hello()
# OP:
# Good Morning!
# Hello World
# Thanks for using Function...

print("\n===================\n")

# Calling decorated add()
add(3, 6)
# OP:
# Good Morning!
# 9
# Thanks for using Function...