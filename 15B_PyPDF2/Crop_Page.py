from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("Read_PDF1.pdf")
writer = PdfWriter()

page = reader.pages[0]

# Set the crop box (x0, y0, x1, y1) – unit is points (1/72 inch)
# Crop to a 300x300 square from the bottom-left
page.mediabox.lower_left = (0, 0)
page.mediabox.upper_right = (300, 300)

writer.add_page(page)

with open("Crop_Page.pdf", "wb") as f:
    writer.write(f)