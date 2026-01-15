"""
This file contains examples of all file modes in Python:
- Text modes: r, w, a, r+, w+, a+, x
- Binary modes: rb, wb, ab
- Using writelines, readline, readlines, etc.

Proper UTF-8 encoding to avoid Unicode errors
"""

import os

# =========================
# TEXT FILE MODES
# =========================

# 1) "w" → Write mode (overwrites file)
#           Creates a new file if it doesn't exist or overwrites existing content
# with open('File_Handling1.txt', 'w', encoding='utf-8') as file:
#     file.write("Hello World\n")               # Writing single line
#     lines = ["Apple\n", "Banana\n", "Cherry\n"]
#     file.writelines(lines)                    # Writing multiple lines at once

# 2) "r" → Read mode (file must exist)
#           Used to read the content of a file
# with open('File_Handling1.txt', 'r', encoding='utf-8') as f:
#     data = f.read()                           # Reads entire file as string
#     # data = f.readline()                     # Reads first line only
#     # data = f.readlines()                    # Reads file into a list of lines
#     print("Reading File:\n", data)

# 3) "a" → Append mode (adds data at end)
#           Adds new data without overwriting existing content
# with open('File_Handling1.txt', 'a', encoding='utf-8') as f:
#     f.write('\nThis is for practice.')       # Append text to the end of file

# 4) "r+" → Read + Write (does not overwrite file)
#           You can read and write. Cursor position is important.
#           .seek(0, 2) → Moves the cursor to the end to append new text.
# with open('File_Handling1.txt', 'r+', encoding='utf-8') as f:
#     data = f.read()                           # Read entire file
#     f.seek(0,2)                                 # Move cursor to the end
#     f.write(data + '\nPython')               # Add new text without deleting old content

# 5) "w+" → Write + Read (overwrites if file exists)
#           Overwrites existing content and allows reading
# with open('File_Handling1.txt', 'w+', encoding='utf-8') as f:
#     f.write('\n\nThis function overwrites')  # Add new text
#     f.seek(0)                                 # Move cursor to start
#     data = f.read()                           # Read new content
#     print("w+ mode file content:\n", data)

# 6) "a+" → Append + Read
#           Appends data at the end, allows reading
# with open('File_Handling1.txt', 'a+', encoding='utf-8') as f:
#     f.write("\nHello World")                  # Append new line
#     f.seek(0)                                 # Move cursor to start to read all content
#     data = f.read()
#     print("a+ mode file content:\n", data)

# 7) "x" → Create new file (error if file exists)
#           Used to create a file safely without overwriting
# try:
#     with open('File_Handling2.txt', 'x', encoding='utf-8') as f:
#         lines = [
#             "x -> Create new file (raises error if already exists)\n",
#             "Use this mode when you want to ensure the file is created ONLY once\n"
#         ]
#         f.writelines(lines)
# except FileExistsError:
#     print("F2.txt already exists!")

# =========================
# BINARY FILE MODES
# =========================

# 8) "rb" → Read binary
# Used to read binary files like images, videos, etc.
if os.path.exists('Images/1.jpg'):
    with open('Images/1.jpg', 'rb') as f:
        data = f.read()
        print("Binary file read successfully.")

# 9) "wb" → Write binary
# Writes binary data to a file
with open('File_Handling1.bin', 'wb') as file:
    file.write(data)                          # data must be in bytes

# 10) "ab" → Append binary
# Appends binary data to the end of a binary file
with open('File_Handling2.bin', 'ab') as fi:
    fi.write(b"\nNew binary Data.")          # Always use b'' for binary string