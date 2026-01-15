# Uses different fonts and font sizes in a PDF using ReportLab

# Import the canvas class to draw on the PDF
from reportlab.pdfgen import canvas

# Import standard A4 page size
from reportlab.lib.pagesizes import A4

# Create a new PDF file named '4_fonts.pdf' with A4 size
c = canvas.Canvas("4_fonts.pdf", pagesize=A4)

# Set font to Helvetica with size 20 (sans-serif)
c.setFont("Helvetica", 20)
c.drawString(100, 800, "Heading - Helvetica 20pt")  # Draw heading text

# Set font to Courier with size 14 (monospaced)
c.setFont("Courier", 14)
c.drawString(100, 770, "Monospaced - Courier 14pt")  # Draw monospace text

# Set font to Times-Roman with size 12 (serif)
c.setFont("Times-Roman", 12)
c.drawString(100, 750, "Regular text - Times Roman 12pt")  # Draw regular text

# Finalize and save the PDF file
c.save()
