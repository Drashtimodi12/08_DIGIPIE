# re.split(pattern, string, maxsplit=0, flags=0)
# Purpose: Splits a string by the occurrences of the regex pattern.
# Returns: List of strings.

import re

# pattern = r"\d"
# mystr = "apple12banana34cherry56date"
# result = re.split(pattern, mystr)
# print(result)

pattern = r"[,]"
mystr = "apple,banana,cherry,date"
result = re.split(pattern, mystr)
print(result)
# OP: ['apple', 'banana', 'cherry', 'date']