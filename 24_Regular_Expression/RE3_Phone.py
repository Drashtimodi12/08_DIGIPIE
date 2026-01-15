# Match an Indian phone number (10 digits).
# Examples:
# 9876543210 ✔
# 09876543210 ✘ (11 digits)
# 98765-43210 ✘

import re

pattern = r"^\+91-\d{10}$"
mystr = "+91-9909449049"
res = re.match(pattern, mystr)
print(res)
# OP: <re.Match object; span=(0, 14), match='+91-9909449049'>



print("\n========================\n")



# Define a regex pattern to match a 10-digit number
p = "^[0-9]{10}$"

# Use re.match() to check if the string "9909449049" matches the pattern
r = re.match(p, "9909449049")

# If the match is None, the number is invalid
if r is None :
    print("Invalid Number.")
else :
    # If the match is not None, the number is valid
    print("Valid Number.")
# OP: Valid Number.