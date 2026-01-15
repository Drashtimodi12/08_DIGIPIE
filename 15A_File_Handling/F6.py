# Task 6: Append + Read (a+)
# Open the file in a+ mode.
# Add 3 new items (e.g., books, movies).
# Use seek(0) and read the entire file.

with open('F5.txt', 'a+') as f:
    f.write("Kiwi")
    f.seek(0)
    data = f.read()
    print(data)