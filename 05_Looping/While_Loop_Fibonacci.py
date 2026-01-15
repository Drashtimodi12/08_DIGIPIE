# Fibonacci series using while loop : 0,1,1,2,3,5,8,13,21,34,55,.... 

length = 10  # Number of terms

# First two numbers
a = 0
b = 1

count = 2  # Since we already have 0 and 1 printed

print(a, b, end=" ")  # Print the first two numbers

while count < length:  # Run until count reaches the required length
    c = a + b  # Next term in the series
    print(c, end=" ")
    a = b   # Update a and b
    b = c   # Update b and c
    count += 1  # Increment count

# OP: 0 1 1 2 3 5 8 13 21 34