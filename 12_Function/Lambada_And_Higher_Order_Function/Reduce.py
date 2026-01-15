# The reduce() function in Python reduces a list to a single value by applying a function repeatedly.
# Syntx: from functools import reduce               reduce(function, iterable)

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

# Summation using reduce()
c = reduce(lambda x, y : x + y, data)
print(c)        # Output: 76


# Finding the Maximum Value using reduce()
def max(x, y):
    if x > y :
        return x
    else:
        return y

k = reduce(max, data)
print(k)            # Output: 41


# Finding the Minimum Value using reduce()
k = reduce(lambda x, y : x if x < y  else y, data)
print(k)            # Output: 1