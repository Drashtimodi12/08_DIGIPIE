# Recursive Function in Python:- Your function call(a) is a recursive function, meaning it calls itself until a condition is met.

def call(a):
    print(a * a)  # Print square of 'a'
    a += 1  # Increment 'a' by 1
    if a < 20:  # Check if 'a' is less than 20
        call(a)  # Recursive call

call(10)  # Initial function call with a = 10

# Output:
# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361