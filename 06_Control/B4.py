# Break with For Loop
# Iterate through a list of strings ["apple", "banana", "cherry", "date"]
# Stop printing when you find "cherry" using break.

a = ["apple", "banana", "cherry", "date"]
for i in a:
    if i == 'cherry':
        break
    else:
        print(i)
# OP:
# apple
# banana