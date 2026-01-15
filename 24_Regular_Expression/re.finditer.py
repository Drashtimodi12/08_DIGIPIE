# re.finditer(pattern, string, flags=0)
# Purpose: Returns an iterator of match objects for all matches.
# Useful when you want match positions.

import re 

# pattern = r"[A-z][a-z]+"
# mystr = "Hello my Name is Drashti"
# result = re.finditer(pattern, mystr)

# for same in result:
#     print("\n", same.group(), "starts at", same.start(), "ends at", same.end() )


pattern = r"Hello"
mystr = "I am Drashti. Hello all guest."
result = re.finditer(pattern, mystr)

for same in result:
    print("\n", same.group(), "starts at", same.start(), "ends at", same.end() )
# OP:
#  Hello starts at 14 ends at 19