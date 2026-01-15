# Task 8: Binary File Copy
# Read a file image.jpg in rb mode.
# Copy its content to image_copy.jpg using wb mode.

with open('Images/1.jpg', 'rb') as f:
    data = f.read()

with open('Images/2.jpg', 'wb') as f:
    f.write(data)