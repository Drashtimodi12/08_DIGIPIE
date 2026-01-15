# Input a list of numbers and calculate the product of all elements using a loop.

a = [1, 2, 3, 4]
m = 1
for i in a:
    m *= i
print("Product of all elements: ", m)
# OP: Product of all elements:  24

print("\n====================\n")




while i < len(a) :
    m *= a[i]
    i += 1

print("Product of all elements: ", m)
# OP: Product of all elements:  24
