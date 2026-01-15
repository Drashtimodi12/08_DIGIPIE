# Write a function that counts vowels in a string.

def myfun(a):
    vowels = 'aeiou'
    count = 0
    for ch in a:
        if ch in vowels:
            count += 1
    return count

print(myfun('my name is drashti'))
# OP: 5