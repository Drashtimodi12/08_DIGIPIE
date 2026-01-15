# Create a function that accepts a list and returns the sum of all numbers.

def num(l):
    result = sum(l)
    return result
a = [1,4,6,2]
print("Sum of list number is ", num(a))
# OP: Sum of list number is  13
print("\n==================\n")



def num(l):
    total = 0
    for i in l:
        total += i
    return total
a = [1,4,6,2]
print("Sum of list number is ", num(a))
# OP: Sum of list number is  13