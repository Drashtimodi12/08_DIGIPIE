# Function that reverses a string using recursion.

# def st(a):
#     b = a[::-1]
#     print(' '.join(b))

# d = input("Enter string: ").lower()
# st(d)

def reverse(a):
    if a == "":
        return a
    else:
        return reverse(a[1:]) + a[0] 
        # return reverse("at") + "c" -> return reverse("t") + "a" -> return reverse("") + "t"

word = input("Enter string: ").lower()
print(reverse(word))
# OP:
# Enter string: 213
# 312