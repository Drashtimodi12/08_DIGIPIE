"""    -------2. filter() Function------
Filters elements from an iterable based on a condition (True/False).
A filter object (convert to list to see results).

Syntax: filter(function, iterable)

Why use filter?     “Filter elements that satisfy this condition.”
"""

# Use filter() and lambda to get even numbers from a list.

num = [1, 2, 3, 4, 5]
a = list(filter(lambda x : x % 2 == 0, num))
print(a)
# OP: [2, 4]

print("\n=====================\n")

a = lambda x : x % 2 == 0
x = [1, 2, 3, 4, 5]
print(list(filter(a, x)))
# OP: [2, 4]

print("\n=====================\n")

# Use lambda and filter() to keep only numbers greater than 50 from a list.
l = [100, 56, 102, 565, 21]
result = list(filter(lambda x : x > 50, l))
print(result)
# OP: [100, 56, 102, 565]
print("\n=====================\n")

# Use filter() to extract all palindromes from a list of strings.
l2 = ['POP', 'apple', 'Mom']
result = lambda x : x.upper() == x.upper()[::-1]    # Because original casing stays, but comparison happens in upper
print(list(filter(result, l2)))
# OP: ['POP', 'Mom']