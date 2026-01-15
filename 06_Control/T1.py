# Combined Task
# Take numbers from 1 to 20
# Skip even numbers (continue)
# Stop if the number is greater than 15 (break)
# Print remaining numbers.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    elif i > 15:
        break
    else:
        print(i)
# OP:
# 1
# 3
# 5
# 7
# 9