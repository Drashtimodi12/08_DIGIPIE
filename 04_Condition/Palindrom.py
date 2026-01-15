n = input("to check palindrome: ")

if n == n[::-1]:
    print(f"{n} is a Palindrome.")
else:
    print(f"{n} is not a Palindrome.")
# OP:
# to check palindrome: 12
# 12 is not a Palindrome.