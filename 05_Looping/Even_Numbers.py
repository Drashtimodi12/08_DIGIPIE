# Given a list of numbers, create a new list containing only even numbers using a loop.


a = [1, 2, 3, 4, 5, 6]

for i in a:
    if i % 2 != 0:
        a.remove(i)
print(a)        # OP: [2, 4, 6]

print("\n====================\n")


b =[]
i = 0 
while i < len(a):
    if i % 2 == 0:
        b.append(a[i])
    i += 1
print(b)    # OP: [2, 6]