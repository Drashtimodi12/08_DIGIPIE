# 34.	Write a Python program that filters out even numbers using the filter() function.

def even(n) :
    return n % 2 != 0

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # List of numbers

number = list(filter(even, n))          # Use filter() to filter out even numbers

print("Filtered even Number: ", number)     # Print the filtered list
# Output: Filtered even Number:  [1, 3, 5, 7, 9]