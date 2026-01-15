"""
re.search(pattern, string, flags=0)
Purpose: Searches for the first occurrence of the pattern anywhere in the string.
Returns: Match object if found, else None.
"""

import re

# pattern = "Python"
# mystr = "Hello World. Here is Python Programming."
# a = re.search(pattern, mystr)
# print(a)




# [A-Za-z]+ → one or more letters
# \d+       → one or more digits
pattern = r"[A-Za-z]+\d+"
mystr = "abc123 adc"
result = re.search(pattern, mystr)
if result:
    print(result.group())  # whole matched string
else:
    print("No match found")
# OP:
# abc123