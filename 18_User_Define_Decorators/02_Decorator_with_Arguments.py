# 2. Decorator with Arguments:-   Here, the decorator itself takes arguments.


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()
# OP:
# Hello
# Hello
# Hello

print("\n=============================\n")


# Add two numbers using a decorator
def add(fun):
    # This function will wrap the original function
    def start(a, b):
        print("Welcome")

        # Check if both a and b are numbers using isinstance()
        # Correct syntax: isinstance(value, (type1, type2))
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            print("Invalid Input")
            return
        else:
            # If valid numbers, call the original function
            fun(a, b)

        print("Thank you\n")

    return start


@add   # Applying decorator
def calculation(a, b):
    # This function only performs addition
    print(f"{a} + {b} = {a + b}")


# Function call
calculation(4, 5)
# OP: 
# Welcome
# 4 + 5 = 9
# Thank you