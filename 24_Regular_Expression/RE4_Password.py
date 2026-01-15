# Match a password with all conditions:
# at least 1 uppercase
# at least 1 lowercase
# at least 1 digit
# at least 8 characters
# Examples:
# Hello123 ✔
# hello123 ✘

import re
# ^(?=.*[A-Z])      # Lookahead: ensures at least ONE uppercase letter exists anywhere in the string
# (?=.*[a-z])       # Lookahead: ensures at least ONE lowercase letter exists anywhere
# (?=.*\d)          # Lookahead: ensures at least ONE digit exists anywhere
# .{8,}$            # The entire password must be at least 8 characters long
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
mystr = "heL1lomodi"
res = re.match(pattern, mystr)

print(res)
# OP: <re.Match object; span=(0, 10), match='heL1lomodi'>