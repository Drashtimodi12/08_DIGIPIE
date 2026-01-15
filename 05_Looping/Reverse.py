# Input a number and reverse it using a loop.

# num = int(input("Enter a number to reverse: "))
num = 102
rev = 0
while num > 0:
    digit = num % 10       # Get last digit
    rev = rev * 10 + digit # Add digit to reverse number
    num //= 10             # Remove last digit

print("Reversed number:", rev)
   
# OP:
# Reversed number: 201