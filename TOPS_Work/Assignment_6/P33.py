# 33.	Write a Python program that uses reduce() to find the product of a list of numbers.

# Multiplication using reduce()
from functools import reduce

data = [1, 3, 5, 7, 9, 10, 41]

def add(x, y):
    print(x, y)      # Prints intermediate values
    return x * y

c = reduce(add, data)
# Output:
# 1 3
# 3 5
# 15 7
# 105 9
# 945 10
# 9450 41

# Using reduce() with lambda (shortest way)
product_lambda = reduce(lambda x, y: x * y, data)
print(product_lambda)  # Output: 387450