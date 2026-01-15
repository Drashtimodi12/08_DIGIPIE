# Save Extracted Text to File
# Opens a PDF file and reads through every page.
# Uses extract_text() to get readable text content (not images).
# Writes the extracted text to a file named output.txt, one page per line (with an extra line break).
# If a page has no extractable text (like scanned images), extract_text() will return None, so those pages are skipped.

import pdfplumber


# UTF-8 stands for Unicode Transformation Format – 8-bit.
# It can represent all characters in the Unicode standard, including:
# English letters and numbers
# Special characters (€, ©, ™, etc.)
# Non-English scripts (Hindi, Chinese, Arabic, etc.)

# Open the PDF file "example.pdf" and also open a text file "output.txt" for writing extracted text
with pdfplumber.open("Text_Img.pdf") as file, open("Extract_Text_To_File.txt", "w", encoding="utf-8") as output:

    # Iterate through each page in the PDF
    for page in file.pages:

        # Extract text from the current page
        text = page.extract_text()

        # If text is found (i.e., not None), write it to the output file
        if text:
            output.write(text + "\n")  # Write the extracted text followed by a newline