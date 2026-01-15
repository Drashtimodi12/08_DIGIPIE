"""
r-string (Raw String) = Prefix: r"..." or R"..."
A raw string treats backslashes (\) as normal characters and does NOT escape them.

✔ Use when writing:
File paths
Regular expressions
"""

path = (r"My gamil id is = 'drashti@gmail.com'.")
print(path)
# OP: My gamil id is = 'drashti@gmail.com'.