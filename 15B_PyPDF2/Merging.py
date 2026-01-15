from PyPDF2 import PdfReader, PdfWriter
import PyPDF2

# Create a PdfWriter object to store the merged PDF pages
pdf_writer = PdfWriter()

# List of PDF files to be merged
for file in ['Read_PDF1.pdf', 'Read_PDF2.pdf']:
    reader = PdfReader(file)        # Create a PdfReader object for each file

    # Loop through all the pages in the current PDF file
    for page in reader.pages:  
        pdf_writer.add_page(page)    # Add each page to the PdfWriter object


# Write the combined pages into a new PDF file
with open("Merging.pdf", "wb") as outputfile:
    pdf_writer.write(outputfile)            # Save the merged content to 'merged.pdf' in write-binary mode

