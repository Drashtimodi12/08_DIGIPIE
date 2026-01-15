# Task 4: Read + Write (r+)
# Open the file in r+ mode.
# Read existing content, then add a new line: "I love Python".
# Print final content.

with open('F1.txt', 'r+') as f:
    data = f.read()
    f.seek(0,2)
    f.write('\nI love Python.')
    f.seek(0)
    print(data)