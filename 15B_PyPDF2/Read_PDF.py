import PyPDF2       # Import the PyPDF2 library to work with PDF files


# with open('Read_PDF1.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)

#     for page in reader.pages:
#         print(page.extract_text())

# ---------------------------------------------------------------------------------------------------------------



# with open("Read_PDF1.pdf", "rb") as file:    # Open the PDF file in binary read mode ('rb')
#     reader = PyPDF2.PdfReader(file)                    # Create a PdfReader object to read the PDF file
#     total_pages = len(reader.pages)                     # Get the total number of pages in the PDF
#     print("Total number of pages:", total_pages)

    # # Read the content of the first page
    # first_page = reader.pages[0]
    # text = first_page.extract_text()
    # print(text)

# ---------------------------------------------------------------------------------------------------------------



with open("Watermarks.pdf", "rb") as file:    # Open the PDF file in binary read mode ('rb')
    reader = PyPDF2.PdfReader(file)                    # Create a PdfReader object to read the PDF file
    total_pages = len(reader.pages)                     # Get the total number of pages in the PDF
    print("Total number of pages:", total_pages)

# Go through each page and extract the text
    for page_num in range(total_pages):
        page = reader.pages[page_num]       # Get a specific page using its index (starting from 0)
        text = page.extract_text()          # Extract the text from that page

        # Print the page number and its text
        print(f"\n----------------- Page Number: {page_num + 1} ------------------------")
        print(text)