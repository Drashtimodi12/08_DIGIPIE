# 42.	Write a python program to sum of the first n positive integers. 

# Taking input from user
n = int(input("Enter a positive integer: "))

# Calculating sum using the formula: sum = n * (n + 1) / 2
sum = n * (n + 1) // 2

# Displaying the result
print("Sum of first", n, "positive integers is:", sum)
