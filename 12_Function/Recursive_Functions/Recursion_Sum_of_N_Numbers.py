# 8. Recursive Function (Function calling itself)
def myfun8(n):
    if n <= 1:
        return 1
    else:
        return n + myfun8(n - 1)
print("The sum is", myfun8(5))
# Output: The sum is 15

print("\n===============================\n")

# Return the sum of numbers from 1 to n using recursion.
def num(a):
    if a <= 1:
        return 1
    else:
        return a + num(a-1)
    # → return 3 + num(2) → return 2 + num(1) → return 1   ← base case
print(num(8))
# OP: 36
print("\n===============================\n")

# Write a recursive function that takes a number and returns the sum of its digits.
def n(a):
    if a == 0:
        return 0
    else:
        return a % 10 + n(a // 10)

print(n(123))
# OP: 6
