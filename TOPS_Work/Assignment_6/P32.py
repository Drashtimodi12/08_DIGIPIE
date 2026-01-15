# 32.	Write a Python program to apply the map() function to square a list of numbers.

def square(a):
    b = int(a)
    return b * b

l = [10, 20, 30, 40, 50, 60]

# Using a for-loop
l1 = []
for i in l:         
    k = square(i)
    l1.append(k)
print(l1)           # Output: [100, 400, 900, 1600, 2500, 3600]


# Using map() function (better way)
l2 = map(square, l)
print(list(l2))         # Output: [100, 400, 900, 1600, 2500, 3600]

# Using map() with lambda (shortest way)
l3 = list(map(lambda x : x * x, l))
print(l3)               # Output: [100, 400, 900, 1600, 2500, 3600]