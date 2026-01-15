s = {10, 20, 30}


# Add element 40
s.add(40)
print(s)        # {40, 10, 20, 30}

print("------------------------")

# Remove element 20
s.remove(20)
print(s)        # {40, 10, 30}

print("------------------------")

# Find union with {30,40,50}
u = {30,40,50}
s1 = s.union(u)
print(s1)       # {50, 40, 10, 30}

print("------------------------")

# Find intersection with {20,30,60}
v = {20,30,60}
s2 = s.intersection(v)
print(s2)       # {30}