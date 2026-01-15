# Extract Text from a Specific Page

import pdfplumber

# Open the PDF file named "Text.pdf"
with pdfplumber.open("Text.pdf") as file: 

    # Access the first page of the PDF (index 0 means the first page)      
    page = file.pages[1]

    # Extract the text content from that page
    text = page.extract_text()

    # Print the extracted text from the first page
    print(text)
