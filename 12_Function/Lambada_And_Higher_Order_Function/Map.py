# Understanding map() Function:-
# Syntax: map(function, iterable)
# function → A function to apply to each item in the iterable.
# iterable → The sequence (like a list or tuple) whose elements the function will process.


# -----------------------------------------------
# Function to Calculate the Square of a Number
# Using map() to Apply the square() Function to a List
# -----------------------------------------------
def square(a):
    b = int(a)
    return b * b

l = [10, 20, 30, 40, 50, 60]

l1 = []
for i in l:         # Using a for-loop (old way)
    k = square(i)
    l1.append(k)
print(l1)           # Output: [100, 400, 900, 1600, 2500, 3600]




# -----------------------------------------------
# Using map() function (better way)
# -----------------------------------------------
l1 = map(square, l)
print(list(l1))         # Output: [100, 400, 900, 1600, 2500, 3600]




# -----------------------------------------------
# Taking user input and applying map()
# -----------------------------------------------
l1 = list(map(square, input("Enter numbers: ").split()))
print(l1)
# Input: 2 3 4
# Output: [4, 9, 16]




# -----------------------------------------------
# Function to Add 1 to a Number
# Using apply() to Pass a Function as an Argument
# -----------------------------------------------
def add(x):
    return x + 1

def apply(fun, x):
    return fun(x)

k = apply(add, 10)  # Calls add(10)
print(k)  # Output: 11



# -----------------------------------------------
# Using map() with Lambda Functions
# -----------------------------------------------
l = [1, 2, 3, 4, 5]

l1 = map(lambda x: x * x, l)    
print(list(l1))         # Output: [1, 4, 9, 16, 25]




# -----------------------------------------------
# Using map() with Two Lists
# -----------------------------------------------
a = [10, 20, 30, 40, 50, 1, 3, 4, 5]
b = [1, 2, 3, 4, 5]

c = map(lambda x, y: x + y, a, b)
print(list(c))           #  Output: [11, 22, 33, 44, 55]