import time   # Import time module to measure how long code takes
import numpy as np  # Import NumPy library for fast array operations

# -------------------------------
# Using Python lists
# -------------------------------
list1 = [4, 2, 6, 34, 56]   # First list of numbers
list2 = [89, 34, 9, 2, 70]  # Second list of numbers

start = time.time()  # Start the timer
# Add elements one by one using a loop (list comprehension)
# zip(list1, list2) pairs elements: (4,89), (2,34), (6,9), (34,2), (56,70)
# x + y adds each pair
result_list = [x + y for x, y in zip(list1, list2)]         # Result: [93, 36, 15, 36, 126]
end = time.time()  # End the timer

print("Python list time:", end - start, "seconds")  # Show how long it took

# -------------------------------
# Using NumPy arrays
# -------------------------------
# Convert lists to NumPy arrays for element-wise operations
arr1 = np.array(list1)  # First array
arr2 = np.array(list2)  # Second array

start = time.time()  # Start the timer
# Add arrays directly (NumPy does element-wise addition automatically)
result_array = arr1 + arr2
end = time.time()  # End the timer

print("NumPy array time:", end - start, "seconds")  # Show how fast NumPy is
