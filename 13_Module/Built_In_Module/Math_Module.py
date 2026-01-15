"""
What is Math Module?
It is used to do a mathematical task in python by importing "math".

Math module Operation:-
Factorial(): this function return factorial number.
Ceil(): This function is used to round up of the integer.
Floor(): This function is used to round down of the integer.
Sqrt(): This function is used to return square root of the value.

from math import functionname
import math
"""


import math


# ------1. Factorial()--------
print(math.factorial(5))    # Output: 120
print(math.factorial(10))   # Output: 3628800

# ------2. Ceil()-------- up value
print(math.ceil(1.4))       # Output: 2
print(math.ceil(5.6))       # Output: 6
print(math.ceil(-9.4))      # Output: -9

# ------3. Floor()-------- down value
print(math.floor(0.6))        # Output: 0
print(math.floor(4.6))        # Output: 4

# ------4. Sqrt()--------
print(math.sqrt(8))                 # Output: 2.8284271247461903
print(f"{math.sqrt(8):.2f}")        # Output: 2.83
print(math.sqrt(100))               # Output: 10.0
print(math.isqrt(15))               # Output: Integer square root of 15 = 3
print(math.sqrt(25).is_integer())   # Output: True (since sqrt(25) is a whole number)

# ------5. pow()--------
print(math.pow(2,4))         # Output: 2^4 = 16.0

# ------6. round()--------
print(round(2.4))            # Output: Rounds to nearest integer (2)

# ------7. pi()--------
print(math.pi)               # Output: Value of π = 3.141592653589793