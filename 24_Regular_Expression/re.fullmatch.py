# re.fullmatch(pattern, string, flags=0)
# Purpose: Checks if the entire string matches the pattern.
# Returns: Match object if full match, else None.

import re

# pattern = r"[a-z]+"
# mystr1 = "hello"
# result1 = re.fullmatch(pattern, mystr1)
# if result1:
#     print("Full match found:", result1.group())
# else:
#     print("No full match")




pattern = r"[A-Za-z]+\d+"
mystr = "Hello123"
result = re.fullmatch(pattern, mystr)
if result:
    print("Full match found:", result.group())
else:
    print("No full match")
# OP:
# Full match found: Hello123