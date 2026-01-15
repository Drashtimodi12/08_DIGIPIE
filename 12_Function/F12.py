# Write a function that removes duplicates from a list.

def myfun(lst):
    return list(set(lst))

print(myfun([1, 5, 3, 7, 2, 1, 5, 5]))
# OP: [1, 2, 3, 5, 7]