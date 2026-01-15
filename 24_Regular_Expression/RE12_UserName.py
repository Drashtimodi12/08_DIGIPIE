import re  # The re module provides support for regular expressions in Python.

# Use re.match to check if the string "drashti" matches the pattern "^[A-Za-z]+$"
u = re.match("^[A-Za-z]+$", "drashti")

# If the match is None, the username is invalid
if u is None:
    print("Invalid Username.")
else:
    # If the match is not None, the username is valid
    print("Valid Username.")
# OP: Valid Username.