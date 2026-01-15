# Task 10: File Info
# Use os module to:
# Check if student.txt exists
# Get absolute path
# Get file size
# Rename the file to student_info.txt
# Delete it (optional)

import os

if not os.path.exists('F10.txt'):
    a = os.open('F10.txt', os.O_CREAT)
    os.close(a)
    print("F10.txt File is created.")
else:
    print("F10.txt File is already created")

b = os.path.abspath('F10.txt')
print('F10.txt File Path is: ',b)

c = os.path.getsize('F10.txt')
print('F10.txt File size is: ', c)

d = os.rename('F10.txt', 'Fi10.txt')
print('F10.txt File name is changed.')

os.remove('F10.txt')
print("F10.txt file is deleted.")