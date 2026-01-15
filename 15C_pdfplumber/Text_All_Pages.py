# Extract Text from All Pages
import pdfplumber

# Open the PDF file named "Text.pdf" using a context manager. 'file' will represent the opened PDF document
with pdfplumber.open("Text.pdf") as file:
        
    # Loop through all pages in the PDF using enumerate, 'page_num' is the page number (starting from 1), 'page' is the page object containing the content
    for page_num, page in enumerate(file.pages, start=1):  

        # Extract the text content from the current page
        text = page.extract_text()

        # Print the page number and the extracted text
        print(f"\n-----------------Page Number: {page_num}----------------------\n{text}")
