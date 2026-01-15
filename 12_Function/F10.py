# Write a function to reverse a string (without slicing).

def myfun(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

print(myfun('Drashti Python'))
# OP: nohtyP ithsarD