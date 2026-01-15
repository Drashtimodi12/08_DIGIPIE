# Remove duplicates from list without using set()

a = [1,2,2,3,4,4,5]

new = []
for n in a:
    if n not in new:
        new.append(n)
print(new)          # [1, 2, 3, 4, 5]