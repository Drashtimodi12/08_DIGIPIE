# Match a date in format DD-MM-YYYY.
# Examples:
# 21-10-2024 ✔
# 1-5-24 ✘
# 99-88-7777 ✘

import re
pattern = r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-\d{4}$"
mystr = "21-11-2025"
res = re.match(pattern, mystr)
print(res)
# OP: <re.Match object; span=(0, 10), match='21-11-2025'>