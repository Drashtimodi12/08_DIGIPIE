# Take a number N from the user and calculate the sum of first N natural numbers using a loop.

a = int(input("Enter number: "))
total = 0
for i in range(1, a + 1):
    total += i
print(total)
# OP:
# Enter number: 3
# 6