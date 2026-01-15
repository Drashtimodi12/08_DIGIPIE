# Remove a Specific Page

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("Read_PDF1.pdf")
writer = PdfWriter()

# Let's say we want to remove page 2 (index 1)
for i in range(len(reader.pages)):
    if i != 1:  # Skip page 2
        writer.add_page(reader.pages[i])

with open("Remove_Page.pdf", "wb") as f:
    writer.write(f)
