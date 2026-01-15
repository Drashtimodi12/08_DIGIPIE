# Extract Metadata (Dimensions, Rotation, etc.)

import pdfplumber

with pdfplumber.open("Table.pdf") as file:

    # Iterate through all pages in the PDF using enumerate to get index and page
    for i, page in enumerate(file.pages):

        # Print the width and height of the current page
        print(f"Page {i+1} dimensions: {page.width} x {page.height}")

        # Print the rotation angle of the current page (0, 90, 180, or 270)
        # page.rotation tells you the rotation angle applied to the page, which is useful when processing text or images.
        print(f"Rotation: {page.rotation}")