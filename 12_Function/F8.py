# Write a function that returns factorial of a number.

def myfun(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

print(myfun(5))
# OP: 120