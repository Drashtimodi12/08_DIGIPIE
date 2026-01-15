# Write a function that returns all prime numbers between 1 and n.

def myfun(n):
    prime = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

print(myfun(10))
# OP: [2, 3, 5, 7]