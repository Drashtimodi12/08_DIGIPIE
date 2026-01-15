# Continue with List
# Given a list of numbers [12, 5, 18, 7, 20]
# Print only numbers greater than 10
# Skip numbers less than or equal to 10 using continue.

num = [12, 5, 18, 7, 20]
for i in num:
    if i <= 10:
        continue
    else:
        print(i)
# OP:
# 12
# 18
# 20