# Paragraph with bold/italic using Platypus (Page Layout and Typography Using Scripts)

# Import necessary classes for document and paragraph creation
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Create a SimpleDocTemplate to define the PDF structure and layout
doc = SimpleDocTemplate("7_paragraph.pdf", pagesize=A4)

# Get a set of default paragraph styles (like BodyText, Heading1, etc.)
styles = getSampleStyleSheet()

# Create a Paragraph with inline HTML-style tags for bold <b> and italic <i>
# This uses the "BodyText" style for formatting
para = Paragraph(
    "This is a <b>bold</b> paragraph with <i>italic</i> text using ReportLab's Platypus module.",
    styles["BodyText"]
)

# Build the PDF document using the paragraph as the content
doc.build([para])
