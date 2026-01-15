# Input N and print first N Fibonacci numbers using a loop.

num = int(input("Enter a number: "))

a = 0
b = 1
print(a, b, end = " ")

for i in range(2, num + 1):
    c = a + b
    print(c, end = " ")
    a = b
    b = c
# OP:
# Enter a number: 5
# 0 1 1 2 3 5

print("\n====================\n")

num = int(input("Enter a number: "))

a = 0
b = 1
print(a, b, end = " ")

while num > 2:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    num -= 1
# OP:
# Enter a number: 5
# 0 1 1 2 3 