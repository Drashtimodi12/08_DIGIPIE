# Stop taking input if the user enters -1 using break.

while True:
    num = int(input("Enter 1 or -1: "))
    if num == -1:
        print("Stope the program...")
        break
    else:
        print("Welcome")
# OP:
# Enter 1 or -1: 1
# Welcome
# Enter 1 or -1: -1
# Stope the program...


print("\n-----------------------\n")


# Print the list of entered numbers.
a = []
while True:
    num = int(input("Enter a number (or -1 to stop): "))
    if num == -1:
        print("Stope the program...")
        break
    else:
        a.append(num)
print("Numbers entered:", a)
# OP:
# Enter a number (or -1 to stop): 3
# Enter a number (or -1 to stop): -1
# Stope the program...
# Numbers entered: [3]