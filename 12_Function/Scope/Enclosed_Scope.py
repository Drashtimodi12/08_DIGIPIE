"""
What is an enclosed variable?
It is a variable defined in an outer function that is accessible in an inner function, but not global.
It’s part of nested functions (a function inside another function).
"""

def outer():
    y = 20

    def inner():
        print(y)  # enclosed variable

    inner()

outer()
# OP: 20