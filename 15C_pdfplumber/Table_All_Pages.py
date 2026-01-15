# Extract All Tables from All Pages
 
import pdfplumber

# Open the PDF file named "Table.pdf" for reading
with pdfplumber.open("Table.pdf") as file:

    # Loop through each page of the PDF, 'page_num' gives the page number (starting from 1), 'page' is the actual page object
    for page_num, page in enumerate(file.pages, start=1):

        # Extract all tables on the current page, This returns a list of tables (each table is a list of rows)
        tables = page.extract_tables()

        # Loop through each table found on the current page
        for table in tables:

            # Print a header showing the current page number
            print(f"\n------------- Page Number: {page_num} - Table -------------")

            # Loop through each row in the current table and print it as a list
            for row in table:
                print(row)