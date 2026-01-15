# re.sub(pattern, repl, string, count=0, flags=0)
# Purpose: Replaces matches with a replacement string (repl).
# Returns: Modified string.

import re

# pattern = "Python"
# replace = "Java"
# mystr = "My goal to learn Python Language"
# result = re.sub(pattern, replace, mystr)
# print(result)




# # (\w+) → first word (group 1)
# # (\w+) → second word (group 2)
# pattern = r"(\w+)\s+(\w+)"
# # \2 \1 → replace with second word first, then first word
# replace = r"\2 \1"
# mystr = "Python Language"
# result = re.sub(pattern, replace, mystr)
# print(result)

pattern = r"[aeiouAEIOU]"
replace = "*"
mystr = "My goal to learn Python Language"
result = re.sub(pattern, replace, mystr)
print(result)
# OP: My g**l t* l**rn Pyth*n L*ng**g*