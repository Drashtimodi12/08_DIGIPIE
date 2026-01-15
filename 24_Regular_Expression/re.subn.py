# re.subn(pattern, repl, string, count=0, flags=0)
# Purpose: Same as sub, but also returns number of substitutions/ but it returns a tuple (new_string, number_of_subs_made). 
# Returns: Tuple (new_string, number_of_subs)

import re

# pattern = r"\d"
# replace = "#"
# mystr = "My contact number is 990193223."
# result = re.subn(pattern, replace, mystr)
# print(result)



pattern = r"\s+"
replace = "..."
mystr = "My contact number is 990193223."
result = re.subn(pattern, replace, mystr)
print(result)
# OP: ('My...contact...number...is...990193223.', 4)