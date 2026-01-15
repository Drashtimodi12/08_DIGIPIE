# 37.	Write a Python program to get the Fibonacci series of given range. 

# Fibonacci series using for loop : 0,1,1,2,3,5,8,13,21,34,55,.... 

length = 10  # Number of terms

# First two numbers
a = 0
b = 1

print(a, b, end=" ")    # Print the first two numbers

for i in range(length - 2):  # Loop should run (length-2) times
    c = a + b  # Next term in the series
    print(c, end=" ")
    a = b   # Update a and b
    b = c   # Update b and c