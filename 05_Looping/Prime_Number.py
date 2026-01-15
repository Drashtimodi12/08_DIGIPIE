# Define the number to check for prime


# n = int(input("Enter Number to check number is Prime or Not: "))    

for n in range(2, 21):  # Check prime numbers from 2 to 20
    if n > 1:   #   from 2 because 1 is not a prime number
        for i in range(2, n):       # Check factors from 2 to n-1
            if n % i == 0:          # If n is divisible by any i, it's not prime
                print(n, "is not a Prime Number.")
                break
        else:
            print(n, "is a Prime Number.")       # If the loop completes without breaking, it is a prime number
    else:
        print(n, "is not a Prime Number.")       # Numbers less than or equal to 1 are not prime

# OP:
# 2 is a Prime Number.
# 3 is a Prime Number.
# 4 is not a Prime Number.
# 5 is a Prime Number.
# 6 is not a Prime Number.
# 7 is a Prime Number.
# 8 is not a Prime Number.
# 9 is not a Prime Number.
# 10 is not a Prime Number.
# 11 is a Prime Number.
# 12 is not a Prime Number.
# 13 is a Prime Number.
# 14 is not a Prime Number.
# 15 is not a Prime Number.
# 16 is not a Prime Number.
# 17 is a Prime Number.
# 18 is not a Prime Number.
# 19 is a Prime Number.
# 20 is not a Prime Number.