# We can also add watermark in PDF file if we want. We need another PDF file containing the watermark (like a logo or text). We can overlay this on our main PDF file.
import PyPDF2

# Open the main PDF and watermark PDF in read-binary mode
with open("Read_PDF1.pdf", "rb") as Main, open("Watermark_PDF.pdf", "rb") as watermark:

    # Create PdfReader objects for both the main and watermark PDFs
    reader = PyPDF2.PdfReader(Main)
    watermarker = PyPDF2.PdfReader(watermark)

    # Create a PdfWriter object to store the output (watermarked PDF)
    writer = PyPDF2.PdfWriter()

    # Get the first page of the watermark PDF (assuming watermark is only on the first page)
    watermark_page = watermarker.pages[0]

    # Loop through all pages in the main PDF
    for page in reader.pages:

        # Loop through all pages in the main PDF
        page.merge_page(watermark_page)

        # Add the modified page to the writer
        writer.add_page(page)

    # Write the final output (watermarked PDF) to a file
    with open("Watermarks.pdf", "wb") as output_pdf:
        writer.write(output_pdf)
