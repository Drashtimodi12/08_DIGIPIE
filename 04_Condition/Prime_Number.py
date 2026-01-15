# Check if a given number is prime using a loop.

a = int(input("Enter number to check prime or not: "))

if a <= 1:
    print("Not a Prime number")
else:
    for i in range(2, a):
        if a % i == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime Number.")
# OP:
# Enter number to check prime or not: 2
# Prime Number.