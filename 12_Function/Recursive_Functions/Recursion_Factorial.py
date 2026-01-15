# Recursive Function:
# Write a recursive function factorial(n) that returns the factorial of a given number n.

def fact(a):
    if a == 1:
        return 1
    else:
        return a * (fact(a-1))
    # fact(5) = 5 * 4 = 20 -> fact(4) = 20 * 3 = 60  -> fact(3) = 60 * 2 = 120 -> fact(2) = 120 * 1 =  0

b = int(input("Enter the number for factorial: "))
print(f"The number of factorial is {fact(b)}")

# OP:
# Enter the number for factorial: 5
# The number of factorial is 120