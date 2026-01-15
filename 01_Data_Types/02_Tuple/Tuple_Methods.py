
fruits = ("apple", "banana", "cherry")

# Converting tuple to list, modifying it, and converting back to tuple
l = list(fruits)  # Convert tuple to list
l.append("SQL")  # Add an element
t = tuple(l)  # Convert back to tuple
print("Modified Tuple:", t)  # Output: Modified Tuple: ('apple', 'banana', 'cherry', 'SQL')

# Concatenating two tuples
x = ("test", "tech")
y = ("abc", "xyz")
x += y  # Concatenation
print("Concatenated Tuple:", x)     # Output: Concatenated Tuple: ('test', 'tech', 'abc', 'xyz')

# Tuple unpacking

fruits = ("apple", "banana", "cherry")
(a, *b) = fruits  # Assigns 'a' to first element, 'b' gets the remaining as a list
print("Unpacked values:", b)        # Output: Unpacked values: ['banana', 'cherry']

# Iterating over a tuple
for i in fruits:
    print("Fruit:", i)  # Output: Fruit: apple, Fruit: banana, Fruit: cherry

# Iterating using index
for i in range(len(fruits)):
    print("Fruit at index", i, ":", fruits[i])  # Output: Fruit at index 0 : apple, Fruit at index 1 : banana, Fruit at index 2 : cherry

# Tuple operations
t1 = (10, 20, 30)
t2 = (80, 90, 70)

# Concatenating tuples
t3 = t1 + t2
print("Concatenated Tuple:", t3)    # Output: Concatenated Tuple: (10, 20, 30, 80, 90, 70)

# Repeating tuple elements
t3 = t1 * 3
print("Repeated Tuple:", t3)    # Output: Repeated Tuple: (10, 20, 30, 10, 20, 30, 10, 20, 30)
