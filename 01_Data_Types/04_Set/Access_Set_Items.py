# Access Items:- You cannot access items in a set by referring to an index or a key like myset[0].
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
# by using the in keyword.

myset = {"apple", "mango", "orange"}
for i in myset :
    print(i)
# Output: orange
#         apple
#         mango

# To check whether a specific item exists in a set, use the in keyword.
myset = {"apple", "mango", "orange"}
print("banana" in myset)        # Output: False
print("mango" in myset)         # Output: True

# You can also check if an item does not exist in a set using not in.
myset = {"apple", "mango", "orange"}
print("banana" not in myset)        # Output: True
print("mango" not in myset)         # Output: False