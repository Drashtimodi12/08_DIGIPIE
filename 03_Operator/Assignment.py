# Assignment Operators:   =, +=, -=, *=, /=, %=, //=, **=


x = 10
print(x)        # OP: 10

x += 5
print(x)        # OP: 15

x -= 2
print(x)        # OP: 13

x *= 2
print(x)        # OP: 26

x /= 2
print(x)        # OP: 13.0

x %= 4
print(x)        # OP: 1.0

x //= 2
print(x)        # OP: 0.0

x **= 3
print(x)        # OP: 0.0

print("\n===========================\n")



# Take number from user and keep adding 10 using += until number > 50.
a = float(input("Enter number: "))
total = 0
while a <= 50:
    total += a
    print("Current value: ", total)
    a += 10
print("Loop ended. Final Value is ", total)
# OP:
# Enter number: 10
# Current value:  10.0
# Current value:  30.0
# Current value:  60.0
# Current value:  100.0
# Current value:  150.0
# Loop ended. Final Value is  150.0