# 41.	Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

# Taking rwo integer inputs from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Checking conditions
# True = (3 + 2 = 5)
# True = (10 - 5 = 5), False = (4 + 2 = 6) (None of the conditions met)
# True = (7 + 7 = 14)(Both numbers are equal)
if a == b or (a + b == 5) or abs(a - b) == 5:
    print("True")
else:
    print("False")
