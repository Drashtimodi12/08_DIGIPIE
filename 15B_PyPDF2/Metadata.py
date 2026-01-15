import PyPDF2

# PyPDF2 allows us to extract metadata such as the author, title, and creation date:

with open("Read_PDF1.pdf", "rb") as file:
    reader =PyPDF2.PdfReader(file)

    metadata = reader.metadata
    print(f"Author: {metadata.author}")
    print(f"Title: {metadata.title}")
    print(f"Creation Date and Time: {metadata.creation_date}")

# Output: 
# Author: Dhrashti Modi
# Title: None
# Creation Date and Time: 2025-07-20 17:37:12+05:30