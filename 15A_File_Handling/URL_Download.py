"""
pip install requests
pip install pillow
"""
import requests

# Function to download a file from a URL
def download_file(url, file_name):
    response = requests.get(url)      # Send request to the URL
    open(file_name, "wb").write(response.content)  # Save file in binary mode
    print(f"{file_name} downloaded successfully!")

# -------------------------
# Download JPG Image
jpg_url = "https://example.com/image.jpg"
download_file(jpg_url, "my_image.jpg")   # Save as JPG file

# Download PNG Image
png_url = "https://example.com/photo.png"
download_file(png_url, "my_photo.png")   # Save as PNG file

# Download PDF File
pdf_url = "https://example.com/file.pdf"
download_file(pdf_url, "document.pdf")   # Save as PDF

# Download DOCX File
docx_url = "https://example.com/report.docx"
download_file(docx_url, "report.docx")   # Save as DOCX

# Download Excel File
excel_url = "https://example.com/data.xlsx"
download_file(excel_url, "data.xlsx")    # Save as Excel file
