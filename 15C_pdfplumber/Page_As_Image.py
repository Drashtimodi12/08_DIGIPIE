# Save a Page as an Image

import pdfplumber

with pdfplumber.open("Table.pdf") as file:
    
    # Access the first page of the PDF (index 0)
    page = file.pages[0]

    # Convert the page to an image with a resolution of 150 DPI (dots per inch)
    # and save the image as "page_image.png" in the current directory
    page.to_image(resolution=150).save("Page_As_Image.png")