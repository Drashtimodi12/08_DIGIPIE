# Create a class MathUtils with a static method add(a, b) returning their sum, and 
# a class method info(cls) printing "This is a math utility class". 
# Call both methods without creating an object.


class MathUtils:

    @staticmethod
    def add(a, b):
        return f"{a} + {b} = {a + b}"
    
    @classmethod
    def info(cls):
        print("This is a math utility class.")

print(MathUtils.add(10, 1))
MathUtils.info()
# OP:
# 10 + 1 = 11
# This is a math utility class.