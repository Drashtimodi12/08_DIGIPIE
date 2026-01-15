# Task 9: Append Binary
# Open a binary file data.bin in ab mode.
# Append some bytes (e.g., b"\nExtra bytes").
# Read the file in rb mode to verify.

# 1. Open a binary file in append-binary mode
with open('binary1.bin', 'ab') as f:
    f.write(b"\n\nhello World")  # Append bytes at the end

# 2. Open the same file in read-binary mode to verify
with open('binary1.bin', 'rb') as f:
    data = f.read()  # Read all bytes
    print(data)
