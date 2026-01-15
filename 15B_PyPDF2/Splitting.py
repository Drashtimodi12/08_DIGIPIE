# If we want to split a PDF into separate pages, PyPDF2 makes this easy. Let's split the Merging_PDF.pdf file.

import PyPDF2

with open("Merging_PDF.pdf", "rb") as file:       # Open the merged PDF file in read-binary ('rb') mode
    reader = PyPDF2.PdfReader(file)             # Create a PdfReader object to read pages from the PDF

    # Loop through each page in the PDF using enumerate() to get the index (i) and page object
    for i, page in enumerate(reader.pages):
        writer = PyPDF2.PdfWriter()             # Create a new PdfWriter object for each individual page
        writer.add_page(page)                   # Add the current page to the writer

        with open(f'Splitting_{i+1}.pdf', 'wb') as output_pdf:        # Save the current page to a new PDF file named page_1.pdf, page_2.pdf, etc.
            writer.write(output_pdf)                             # Write the page to the output file