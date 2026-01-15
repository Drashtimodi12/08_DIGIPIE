# Print all numbers from 1 to 20 except multiples of 3 using continue.

for i in range(1, 21):
    if i % 3 == 0:
        continue
    else:
        print(i, end = " ")
# OP: 1 2 4 5 7 8 10 11 13 14 16 17 19 20