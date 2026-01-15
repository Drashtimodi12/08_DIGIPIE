# Print first n Fibonacci numbers using recursion.

def fib(a):
    if a <= 1:
        return a
        # fib(1) → 1 -> fib(0) → 0
    else:
        return fib(a-1) + fib(a-2) 
    # fib(5) = fib(4) + fib(3) -> fib(4) = fib(3) + fib(2) -> fib(3) = fib(2) + fib(1) -> fib(1) + fib(0)



for i in range(8):
    print(fib(i), end= " ")
# OP: 0 1 1 2 3 5 8 13 