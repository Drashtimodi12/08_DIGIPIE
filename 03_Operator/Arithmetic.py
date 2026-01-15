# Arithmetic Operators: +, -, *, /, %, **, //

# Addition
print(10 + 10)    # OP: 20


# String concatenation
print("a" + "b")  # OP: ab

# print("a" + 10)   # This will cause a TypeError because you cannot add a string and an integer directly.


# Mixing int and float results in a float (implicit type conversion)
a = 10 + 10.00    
print(type(a))  # OP: <class 'float'>
print(a)        # OP: 20.0


# Modulus: Returns the remainder
print(10 % 3)     # OP: 1


# Exponentiation
print(10 ** 2)    # OP: 100


# Floor Division
print(16 // 3)    # OP: 5


# Using variables for arithmetic operations
x = 10
y = 3

print(x + y)  # Addition: 10 + 3 = 13
print(x - y)  # Subtraction: 10 - 3 = 7
print(x * y)  # Multiplication: 10 * 3 = 30
print(x / y)  # Division: 10 / 3 = 3.3333 (returns a float)
print(x // y)  # Floor Division: 10 // 3 = 3 (returns only the integer part)
print(x % y)  # Modulus: Returns the remainder of 10 ÷ 3 (10 % 3 = 1)
print(x ** y)  # Exponentiation: Raises 10 to the power of 3 (10^3 = 1000)