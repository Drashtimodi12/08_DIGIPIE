from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = "FPDF is a Python library to generate PDF files. You can create headers, paragraphs, and tables easily."
pdf.multi_cell(0, 10, text)

pdf.output("multiline.pdf")
