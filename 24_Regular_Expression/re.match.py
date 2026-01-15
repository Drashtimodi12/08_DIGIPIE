"""
re.match(pattern, string, flags=0)
Purpose: Checks for a match only at the beginning of the string.
Returns: Match object if found, else None.

Only matches from start. "World" won’t match.
"""

import re

# try:
# # \d – Matches any digit (0–9).
#     pattern = r"^\d+$"
#     result = input("Only number allowed: ")
#     a = re.match(pattern, result)
# except Exception as e:
#     print(e)
# finally:
#     if a:
#         print(a)
#     else:
#         print("Invalid input! Only letters are allowed.")



# \d – Matches any single digit (0–9).
# [a-z]+ – Matches one or more lowercase letters from a to z.
# \S+ – Matches one or more whitespace characters (anything except space, tab, newline).
pattern = r"^\d+[a-z]+\s+[A-Za-z]+$"
result = input("Enter to check: ")

a = re.match(pattern, result)
print(a)
# OP:
# Enter to check: 12drashti modi
# <re.Match object; span=(0, 14), match='12drashti modi'>