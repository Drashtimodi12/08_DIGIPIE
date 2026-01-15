# Match an email address.
# Simple rule:
# username@domain.ext
# Examples:
# user123@gmail.com ✔
# user@domain ✘

import re

pattern = r"^[A-Za-z]+\d+@[a-z]+\.[a-z]+$"
mystr = "Drashti33@gmail.com"

res = re.match(pattern, mystr)
print(res)
# OP: <re.Match object; span=(0, 19), match='Drashti33@gmail.com'>