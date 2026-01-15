# Task 1:
# Write three functions:
# download_file()
# process_file()
# save_file()
# Call them one after another synchronously.

import time
import requests
from PIL import Image

# Function 1: Download image and save as Images/1.jpg
def download_file(url):
    print("Downloading image...")
    response = requests.get(url)
    time.sleep(1)

    with open("Images/1.jpg", "wb") as f:
        f.write(response.content)

    print("Download completed. Saved as Images/1.jpg")
    return "Images/1.jpg"   # Return correct path


# Function 2: Open 1.jpg, show image, and read binary data
def process_file(file_name):
    print("\nOpening downloaded image...")
    time.sleep(2)

    # Open and show image using PIL
    img = Image.open(file_name)
    img.show()     # This will open the image viewer

    time.sleep(3)

    # Read image binary data
    with open(file_name, "rb") as f:
        data = f.read()

    print("Image opened and data processed.")
    return data     # Return binary data


# Function 3: Save binary data to binary1.txt
def save_file(data):
    print("\nSaving binary data into text file...")
    time.sleep(2)

    with open("Images/binary1.txt", "wb") as f:
        f.write(data)

    print("File saved as Images/binary1.txt")


# -------------------------------
def main():
    url = "https://picsum.photos/id/13/2500/1667.jpg"

    img_file = download_file(url)
    binary_data = process_file(img_file)
    save_file(binary_data)


# Run program
main()
print("All tasks done synchronously.")
# OP:
# Downloading image...
# Download completed. Saved as Images/1.jpg

# Opening downloaded image...
# Image opened and data processed.

# Saving binary data into text file...
# File saved as Images/binary1.txt
# All tasks done synchronously.