# Simulate downloading 3 images at the same time.
# Steps:
# Create function download_image(name):
# prints "Downloading {name}..."
# waits 3 seconds
# prints "Downloaded {name}!"

import asyncio

async def image(url, n):
    print(f"Start {n} number image to download..")
    await asyncio.sleep(2)
    print(f"Download image is {url}.")

async def main():
    await asyncio.gather(image("image1.jpg", 1), image("image2.jpg", 2), image("image3.jpg", 3))

asyncio.run(main())
# OP:
# Start 1 number image to download..
# Start 2 number image to download..
# Start 3 number image to download..
# Download image is image1.jpg.
# Download image is image2.jpg.
# Download image is image3.jpg.
