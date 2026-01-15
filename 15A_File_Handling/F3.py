# Task 3: Append Data
# Open the file in append mode.
# Add your hobby at the end of the file.
# Read the file afterward to verify.

with open('F1.txt', 'a') as f:
    f.write('Hobby: Nailart')

with open('F1.txt', 'r') as f:
    data = f.read()
    print(data)