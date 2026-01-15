# Adds a Code39 barcode to a PDF using ReportLab

# Import canvas for drawing and A4 page size
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Import barcode module (Code39) from ReportLab graphics
from reportlab.graphics.barcode import code39

# Create a canvas object for the PDF named '8_barcode.pdf'
c = canvas.Canvas("8_barcode.pdf", pagesize=A4)

# Create a Code39 barcode with data "123456789"
# barHeight = 40 defines the height of the bars
# stop=1 adds start/stop characters (*) for valid barcode rendering
barcode = code39.Standard39("123456789", barHeight=40, stop=1)

# Draw the barcode on the canvas at coordinates (100, 700)
barcode.drawOn(c, 100, 700)

# Add a label below the barcode for readability
c.drawString(100, 680, "Barcode: 123456789")

# Finalize and save the PDF document
c.save()
