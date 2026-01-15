# Logical Operator: AND, OR, NOT

a = 10
b = 20

# Logical AND (both conditions must be True)
print(a > 5 and b > 15)  # True (10 > 5 True and 20 > 15 True)
print(a > 5 and b < 15)  # False (10 > 5 True 20 < 15 is False)

# Logical OR (at least one condition must be True)
print(a > 5 or b < 15)  # True (10 > 5 is True, 20 < 15 is False)
print(a < 5 or b < 15)  # False (both 10 < 5 and 20 < 15 are False)

# Logical NOT (reverses the condition)
print(not (a > 5))  # False (10 > 5 is True, but 'not' makes it False)
print(not (b < 15))  # True (20 < 15 is False, but 'not' makes it True)

print("\n===========================\n")






# Check if a person can vote: Age ≥ 18   And must be Indian (country == "India")
a = int(input("Enter your age: "))
c = input("Country: ").upper()

if a >= 18 and c == 'INDIAN':
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# OP:
# Enter your age: 21
# Country: india
# You are not eligible to vote.

print("\n===========================\n")




# Check if a number is positive AND even.
e = float(input("Enter Number: "))
if e >= 0 and e % 2 == 0:
    print("Positive and even")
else:
    print("Not positive and even")
# OP:
# Enter Number: 2
# Positive and even

print("\n===========================\n")




# Write a program using not to flip boolean value.
user = input("Enter True/Flase: ").title()
value = user == "True"
print("Original:", value)
print("Flipped:", not value)
# OP:
# Enter True/Flase: True
# Original: True
# Flipped: False