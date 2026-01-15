"""    -------3. reduce() Function------
Applies a rolling computation to pairs of elements in a sequence —
i.e., it reduces the iterable to a single value.

Its available inside the functools module, so you must import it:       from functools import reduce

Syntax: reduce(function, iterable)

Why use reduce?     “Combine all elements into one value.”
"""
# Use reduce() and lambda to find the product of all numbers in a list.

from functools import reduce

num = [1, 2, 3, 4, 5, 6]
a = reduce(lambda x, y : x + y, num)
print(a)
# OP:21
print("\n=====================\n")

b = lambda x, y : x * y
num = [1, 2, 3, 4, 5, 6]
print(reduce(b, num))
# OP: 720
print("\n=====================\n")

# Use reduce() with a lambda function to find the product of all numbers in the list.

a = [1, 2, 3, 4, 5]
product = reduce(lambda x, y : x * y, a)
print(product)
# OP: 120