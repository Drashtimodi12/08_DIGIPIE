# re.findall(pattern, string, flags=0)
# Purpose: Returns all non-overlapping matches as a list of strings.
# Returns: List of strings (matches).


import re

pattern = r"\."

mystr = "Hello! My name is Drashti."
result = re.findall(pattern, mystr)
if result:
    print("Find dot in the result.")
else:
    print("Not Found result.")

# OP:
# Find dot in the result.