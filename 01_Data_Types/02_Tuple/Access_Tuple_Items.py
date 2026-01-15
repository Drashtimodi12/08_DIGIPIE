# Accessing Tuple Items:
# Tuples are indexed, meaning each item has a specific position in the tuple, inside square brackets.
# Indexing starts from 0 for the first item, 1 for the second, and so on.
# Negative indexing starts from -1 for the last item, -2 for the second last, etc.

mytuple = ("apple", "banana", "cherry", "kiwi", "mango", "orange")
# Accessing elements using index positions
print(mytuple[0:2])         # Output: ('apple', 'banana')
print(mytuple[3])           # Output: cherry
print(mytuple[-2])          # Output: mango

# Slicing a tuple:
print(mytuple[2:5])         # Output: ('cherry', 'kiwi', 'mango')
print(mytuple[-3:-1])       # Output: ('kiwi', 'mango')
print(mytuple[:3])          # Output: ('apple', 'banana', 'cherry')
print(mytuple[2:])          # Output: ('cherry', 'kiwi', 'mango', 'orange')

# Checking if an item exists in a tuple:
# The "in" keyword is used to check for an element in a tuple.
mytuple = ("apple", "banana", "cherry", "kiwi", "mango", "orange")
if "mango" in mytuple :
    print("Yes, 'apple' is in the frutis tuple.")
# Output: Yes, 'apple' is in the frutis tuple.




# tuple[start:end:step] --- Extracts elements from start to end-1, skipping step elements.

# Index   0       1        2       3        4
#        "apple" "banana" "mango" "orange" "kiwi"

# mytuple[1:5:2]
# Start at index 1 → "banana"
# Skip 1 element (step=2) → Next element included is at index 3 → "orange"
# Stop before index 5, so "kiwi" (index 4) is not included.
# Selected elements: ('banana', 'orange')
mytuple = ("apple", "banana", "mango", "orange", "kiwi")

# Access alternate elements using slicing with step 2
print(mytuple[1:5:2])             # Output: ('banana', 'orange')