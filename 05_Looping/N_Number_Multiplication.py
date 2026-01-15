# Input a number N and print its multiplication table up to 10 using a loop.

a = int(input("Enter a Number: "))

for j in range(1, 11):
        print(f"{a} * {j} = {a * j}")
# OP:
# Enter a Number: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

print("\n====================\n")




i = 1
while i <= 10:
    print(a, "x", i, "=", a * i)
    i += 1
# OP:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50