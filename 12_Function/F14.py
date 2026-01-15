# Write a function that takes a dictionary and prints keys with integer values only.

def myfun(d):
    for key, value in d.items():
        if isinstance(value, int) and value > 0:
            print(key, value)

myfun({'d': 1, 'a': -46, 'x': 3.5})
# OP: d 1