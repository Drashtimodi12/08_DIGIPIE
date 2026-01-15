from fpdf import FPDF

pdf = FPDF()
pdf.add_page()  # Add a new page
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Hello, FPDF World!", ln=True, align='C')

pdf.output("basic_hello.pdf")
