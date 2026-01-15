# Demonstrates how to create a multi-page PDF using ReportLab

# Import the canvas class to draw on the PDF
from reportlab.pdfgen import canvas

# Import standard A4 page size
from reportlab.lib.pagesizes import A4

# Create a new PDF named '6_multipage.pdf' with A4 page size
c = canvas.Canvas("6_multipage.pdf", pagesize=A4)

# Loop through page numbers 1 to 3 to create 3 pages
for i in range(1, 4):
    # Write text at the top of each page
    c.drawString(100, 800, f"This is page {i}")
    
    # End the current page and start a new one
    c.showPage()

# Save the complete PDF after all pages are added
c.save()
