# Match a string that starts with 2 digits, has letters in the middle, and ends with 2 special symbols.
# Example:
# 12hello@$ ✔
# 99Hi?? ✔
# 1abc!@ ✘

import re

# [^A-Za-z0-9]{2} → exactly 2 special characters (not letters or digits)
pattern = r"^\d{2}[A-Za-z]+[^A-Za-z0-9]{2}$"

mystr = ["12hello@$", "99Hi??", "1abc!@"]
for i in mystr:
    res = re.match(pattern, i)
    if res:
        print(res)
    else:
        print("No Match")
# OP: 
# <re.Match object; span=(0, 9), match='12hello@$'>
# <re.Match object; span=(0, 6), match='99Hi??'>
# No Match