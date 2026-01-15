# Task 5: Overwrite (w+)
# Open a file in w+ mode.
# Overwrite the file with 5 favorite fruits.
# Read and print the content after writing.

with open('F5.txt', 'w+') as f:
    f.write("Fruits List")
    f.seek(0)

    data = f.read()
    print(data)

    lines = ["Apple\n", "Banana\n", "Mango\n"]
    f.writelines(lines)
    f.seek(0)
    
    a = f.read()
    print(a)