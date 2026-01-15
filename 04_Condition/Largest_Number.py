# Take three numbers and print the largest.

a = float(input("Enter 1 numbers: "))
b = float(input("Enter 2 numbers: "))
c = float(input("Enter 3 numbers: "))

if a >= b and a >= c:
    print(f"Largest number is {a}.")
elif b >= a and b >= c:
    print(f"Largest number is {b}.")
else:
    print(f"Largest number is {c}.")

# OP:
# Enter 1 numbers: 20
# Enter 2 numbers: 3
# Enter 3 numbers: 56
# Largest number is 56.0.