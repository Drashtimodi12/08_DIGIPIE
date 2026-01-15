#  Comparison Operator: ==, !=, >, <, >=, <=

a = 10
b = 5

# Equal to (==)
print(a == 10)  # True
print(b == 10)  # False

# Not equal to (!=)
print(a != b)  # True
print(a != 10)  # False

# Greater than (>)
print(a > b)  # True
print(b > a)  # False

# Less than (<)
print(a < b)  # False
print(b < a)  # True

# Greater than or equal to (>=)
print(a >= 10)  # True
print(b >= 10)  # False

# Less than or equal to (<=)
print(a <= 10)  # True
print(b <= 10)  # True

print("\n===========================\n")




# Take 2 numbers and print which one is greater.
x = float(input("Enter Num1: "))
y = float(input("Enter Num2: "))
if x > y:
    print(f"{x} is greater number")
else:
    print(f"{y} is greater number")
# OP:
# Enter Num1: 12
# Enter Num2: 3
# 12.0 is greater number

print("\n===========================\n")






# Check if user’s age is equal to 18 or not.
age = int(input("Enter your age: "))
if age == 18:
    print("You are exactly 18")
else:
    print("You are NOT 18")
# OP:
# Enter your age: 21
# You are NOT 18

print("\n===========================\n")




# Check if three numbers are in ascending order.
e = 1
f = 5
g = 6
if e < f < g:
    print("Numbers are in ascending order")
else:
    print("Number is not ascending order")
# OP: Numbers are in ascending order