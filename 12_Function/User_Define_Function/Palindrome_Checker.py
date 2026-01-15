# Function that returns True if a given string is palindrome, else False.

def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
b = input("Enter anything to check palindorme: ").upper()
print(f"{palindrome(b)}")
# OP:
# Enter anything to check palindorme: 2
# True