# Given a dictionary of subjects and marks, return the subject with the highest marks.

# def marks(a):
#     sub = max(a, key=a.get)
#     highest = a[sub]
#     return sub, highest
# b = {'maths':30, 'science': 45, 'english': 38}
# sub, highest = marks(b)
# print(f"Subject with highest marks is {sub} with {highest} marks.")


def a(dic):
    sub = ""
    highest_mark = 0
    for subject, mark in dic.items():
        if mark > highest_mark:
            highest_mark = mark 
            sub = subject
    return sub, highest_mark

b = {'maths':30, 'science': 45, 'english': 38}
sub, highest_mark = a(b)
print(f"Subject with highest marks is {sub} with {highest_mark} marks.")
# OP: Subject with highest marks is science with 45 marks.