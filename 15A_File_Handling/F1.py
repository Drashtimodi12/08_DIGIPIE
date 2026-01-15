# Task 1: Create & Write
# Create a file F1.txt in write mode.
# Write your name, age, and city on separate lines.
# Use .write() for one line and .writelines() for multiple lines.


import os

if not os.path.exists('F1.txt'):
    a = os.open('F1.txt', os.O_CREAT)
    os.close(a)
    print('F1.txt File is created.')
else:
    print('F1.txt file already exists.')

with open('F1.txt', 'w') as f:
    f.write("Give Your basic Details...\n")
    lines = [
        'Name: Drashti\n',
        'Age: 21\n',
        'City: Surat\n'
    ]
    f.writelines(lines)
