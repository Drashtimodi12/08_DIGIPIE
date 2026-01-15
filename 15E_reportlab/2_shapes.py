# Draws shapes (rectangle and circle) on a PDF using ReportLab

# Import the canvas class to draw content on the PDF
from reportlab.pdfgen import canvas

# Import standard A4 page size
from reportlab.lib.pagesizes import A4

# Import color utilities for setting fill and stroke colors
from reportlab.lib import colors

# Create a PDF file named '2_shapes.pdf' with A4 page size
c = canvas.Canvas("2_shapes.pdf", pagesize=A4)

# Set the stroke (border) color for shapes to green
c.setStrokeColor(colors.green)

# Draw a rectangle at position x=100, y=700 with width=200 and height=100
# Only the border will be visible as fill is not set yet
c.rect(100, 700, 200, 100)

# Set the fill color for next shape to blue
c.setFillColor(colors.blue)

# Draw a filled circle with center at x=300, y=500 and radius=50
# The 'fill=1' parameter fills the circle with the current fill color
c.circle(300, 500, 50, fill=1)

# Finalize and save the PDF document
c.save()
