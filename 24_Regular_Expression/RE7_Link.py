# Match a URL starting with http or https.
# Examples:
# https://google.com ✔
# http://example.org ✔
# ftp://site.com ✘

import re

pattern = r"^(https|http)\:\/\/[A-Za-z0-9-]+\.[a-z]{2,}$"

mystr = "https://google.com"
res = re.match(pattern, mystr)
print(res)
# OP: <re.Match object; span=(0, 18), match='https://google.com'>