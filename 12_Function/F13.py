# Write a function to calculate Fibonacci series up to n terms.

def myfun(n):
    a = 0
    b = 1
    result = []
    for i in range(1, n + 1):
        result.append(a)
        a, b = b, a + b
    return result
    
print(myfun(6))
# OP: [0, 1, 1, 2, 3, 5]
