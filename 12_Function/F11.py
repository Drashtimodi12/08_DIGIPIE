# Write a function that checks if a string is a palindrome.

def myfun(p):
    return p == p[::-1]

print(myfun('POP'))
# OP: True