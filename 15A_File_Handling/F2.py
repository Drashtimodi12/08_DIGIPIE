# Task 2: Read File
# Open the file you created in read mode.
# Read the file using:
# .read()
# .readline()
# .readlines()
# Print each output to see the difference.


with open('F1.txt', 'r') as f:
    a = f.read()
    f.seek(0)
    b = f.readline()
    f.seek(0)
    c = f.readlines()
    f.seek(0)
    print("Read Function:\n", a)
    print("\nReadline Function:\n", b)
    print("\nReadlines Function:\n", c)