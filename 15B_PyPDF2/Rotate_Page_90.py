from PyPDF2 import PdfReader, PdfWriter

# Load the existing PDF
reader = PdfReader("Read_PDF1.pdf")
writer = PdfWriter()

# Rotate the first page by 90 degrees clockwise
page = reader.pages[0]
page.rotate(90)  # Or use rotate_clockwise(90) in newer versions

# Add the rotated page to writer
writer.add_page(page)

# Save to a new file
with open("Rotate_Page_90.pdf", "wb") as f:
    writer.write(f)
