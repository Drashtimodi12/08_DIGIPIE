# Importing the array module which provides an array data structure
import array

arr = array.array('i', [1, 2, 3])  # integer array
print(arr)      # Output: array('i', [1, 2, 3])

arr = [10, 25, 5, 80, 40]
# arr.remove(max(arr))    
print(max(arr))     # OP: 80
print(arr[::-1])    # OP: [40, 80, 5, 25, 10]

# Sort the array in ascending order
arr.sort()
print(arr)      # OP: [5, 10, 25, 40, 80]

# Sort the array in descending order
arr.sort(reverse=True)    
print(arr)      # OP: [80, 40, 25, 10, 5]

print(sum(arr))     # OP: 160

print("\n---------------\n")





num = [10, 25, 5, 80, 40]

for i in num:
    if i % 2 == 0:
        print(i, "is even" )
    else:
        print(i, "is odd")
# OP: 
# 10 is even
# 25 is odd
# 5 is odd
# 80 is even
# 40 is even

print("\n---------------\n")








a = [1, 2, 3, 4, 5, 6]
even = odd = 0
for num in a:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)
# OP: Even: 3 Odd: 3