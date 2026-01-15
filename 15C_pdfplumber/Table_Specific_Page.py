# Extract Tables from a Page

import pdfplumber

# Open the PDF file named "Table.pdf"
with pdfplumber.open("Table.pdf") as file:

    # Get the first page (index 0 = first page)
    page = file.pages[1]

    # Try to extract a table from the page
    table = page.extract_table()

    # If a table is found, print each row
    if table:
        for row in table:
            print(row)
    else:
        
        # If no table is found, show a message
        print("No table found on the page.")