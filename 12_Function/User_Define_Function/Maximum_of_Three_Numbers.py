# Write a function that accepts three numbers and prints the largest one.

# def num(a, b, c):
#     n = max(a, b, c)
#     print(n)
# num(10, 23, 6)

def num(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(f"The largest number is {largest}.")
num(19, 1, 90)
# OP: The largest number is 90.