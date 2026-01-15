"""
Definition: A decorator is a special function that adds extra functionality to another function without 
            modifying its actual code.
        A decorator wraps another function and allows you to run code before or after the main function executes

We use a decorator with @decorator_name above a function.

Why do we use decorators?
    Add features to a function without modifying its original code
    Clean and readable
    Avoid rewriting the same code again and again
    Good for logging, authentication, timing, access control, etc.
"""

def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()

# OP:
# Before the function
# Hello!
# After the function