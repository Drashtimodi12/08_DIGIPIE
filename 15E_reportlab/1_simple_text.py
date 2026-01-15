# Draws simple text

# Importing the canvas class from reportlab to draw on PDF
from reportlab.pdfgen import canvas

# Importing standard A4 page size
from reportlab.lib.pagesizes import A4

# Create a new PDF file named "1_simple_text.pdf" with A4 page size
# The canvas object provides methods to draw on the PDF
c = canvas.Canvas("1_simple_text.pdf", pagesize=A4)

# Draw a string (text) at x=100, y=800 on the PDF
# (0,0) is the bottom-left corner of the page
c.drawString(100, 800, "Hello, ReportLab!")

# Save and close the PDF file
# This finalizes the document and writes it to disk
c.save()
