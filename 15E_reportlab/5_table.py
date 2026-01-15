# Creates a table with custom styling using ReportLab's Platypus module

# Import classes for document structure, table creation, and styles
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# Create a SimpleDocTemplate object for PDF generation
# This allows adding multiple flowable elements like tables, paragraphs, etc.
doc = SimpleDocTemplate("5_table.pdf", pagesize=A4)

# Define table data as a list of rows, where each row is a list of columns
data = [['ID', 'Name', 'Marks'],    # Header row
        ['1', 'Alice', '85'],
        ['2', 'Bob', '90'],
        ['3', 'Charlie', '88']]

# Create the table object using the data
table = Table(data)

# Apply styling to the table
table.setStyle(TableStyle([
    # Set background color for header row (row 0)
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),

    # Set text color for header row
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

    # Draw grid lines for all cells
    ('GRID', (0, 0), (-1, -1), 1, colors.black),

    # Align text to the center for all cells
    ('ALIGN', (0, 0), (-1, -1), 'CENTER')
]))

# Build the document with the styled table
doc.build([table])
