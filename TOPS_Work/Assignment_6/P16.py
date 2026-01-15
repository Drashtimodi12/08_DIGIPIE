# 16.	Print this pattern using nested for loop: markdown Copy code
# *
# **
# ***
# ****
# *****

lines = 5  # Number of rows

for i in range(lines):  # Outer loop for rows
    for j in range(i + 1):  # Inner loop for columns (increases with each row)
        print('*', end=' ')  # Print star with space
    print()  # Move to the next line after each row 