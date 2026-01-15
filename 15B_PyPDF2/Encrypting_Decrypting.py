# We can also password-protect our PDF files using encryption.

import PyPDF2

# -----------------------------
# Step 1: Encrypt the PDF
# -----------------------------


# Create a PdfWriter object to build the new (encrypted) PDF
writer = PyPDF2.PdfWriter()

# Open the original PDF in read-binary mode
with open("Read_PDF1.pdf", "rb") as file:
    # Create a PdfReader object to read the existing PDF
    reader = PyPDF2.PdfReader(file)

    # Add all pages from the original PDF to the writer
    for page in reader.pages:
        writer.add_page(page)

# Encrypt the new PDF with a password
writer.encrypt("123")

# Save the encrypted PDF to a new file
with open("Encrypting_Decrypting.pdf", "wb") as Output_file:
    writer.write(Output_file)

# -----------------------------
# Step 2: Decrypt and Read the PDF
# -----------------------------


with open('Encrypting_Decrypting.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Check if PDF is encrypted
    if reader.is_encrypted:
        # Try to decrypt using the correct password
        if reader.decrypt("123"):
            # Loop through pages and extract text
            for page in reader.pages:
                print(page.extract_text())
        else:
            print("Wrong password! Cannot decrypt.")
    else:
        # If not encrypted, just read normally
        for page in reader.pages:
            print(page.extract_text())