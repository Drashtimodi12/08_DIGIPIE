# =========================
# ADDITIONAL FILE HANDLING FUNCTIONS
# =========================
# These functions are useful for checking, deleting, renaming files,
# getting file info, and working with the file cursor.
# Proper UTF-8 encoding is used to avoid Unicode errors when reading/writing.

import os

# -------------------------
# 1) Create an empty file
# -------------------------
fd = os.open('File_Handling3.txt', os.O_CREAT)  # O_CREAT creates the file if it doesn't exist
os.close(fd)  # Close the file descriptor
print(f"Empty file created successfully!")


# -------------------------
# 1) Check if a file exists
# -------------------------
#           open(file_path, 'w') opens the file in write mode. If the file doesn't exist, it creates it.
#           .close() ensures the file is closed immediately, keeping it empty.
#           os.path.exists() returns True if the file/folder exists, otherwise False
if not os.path.exists('File_Handling1.txt'):
    open('File_Handling1.txt', 'w').close()  # Create empty file
    print(f"Empty file 'File_Handling1.txt' created successfully!")
else:
    print(f"File 'File_Handling1.txt' already exists.")


# -------------------------
# 2) Delete a file
# -------------------------
#           os.remove() deletes the specified file permanently
a = os.remove('Images/2.jpg')    # Deletes the file
print("File deleted successfully.", a)   # 'a' is None because remove() returns nothing

# -------------------------
# 3) Rename a file
# -------------------------
#           os.rename(old_name, new_name) renames the file
b = os.rename('File_Handling1.txt', 'File_Handling3.txt')   # Rename F1.txt to F3.txt
print("File name changed.", b)       # 'b' is None because rename() returns nothing

# -------------------------
# 4) Get absolute path
# -------------------------
#           os.path.abspath(filename) returns full path of the file
print("Absolute path of File_Handling1.txt:", os.path.abspath('File_Handling2.txt'))

# -------------------------
# 5) Get file size
# -------------------------
#          os.path.getsize(filename) returns size in bytes
print("File Size is:", os.path.getsize('File_Handling1.txt'), "bytes")

# -------------------------
# 6) Using tell() and seek()
# -------------------------
#           tell() returns the current position of the file pointer
#           seek(position) moves the file pointer to the specified byte
with open('File_Handling1.txt', 'r', encoding='utf-8') as f:
    f.seek(5)                                  # Move pointer to the 5th byte
    print("File pointer at 5th byte:", f.tell())  # Current pointer position
    print("Reading from 5th byte onwards:\n", f.read())  # Read from current pointer
