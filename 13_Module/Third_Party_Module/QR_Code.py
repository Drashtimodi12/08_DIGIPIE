# import qrcode
# from PIL import Image

# print("Libraries installed successfully!")


import qrcode

# Link je QR code ma convert karvu chho
url = "https://nuvuniversity-my.sharepoint.com/:f:/g/personal/dhruvin_pastagia_nuv_ac_in/Eo2WLHR6rERFvL-UzP2RG9IBzUGjIpe837voZFNG31GLCw?e=XZ3WKG"

# QR code generate karva mate
qr = qrcode.QRCode(
    version=1,  # QR code no size (1 thi 40 sudhi)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Box ni size
    border=4,  # Border ni size
)

qr.add_data(url)
qr.make(fit=True)

# Image banavva mate
qr_img = qr.make_image(fill="black", back_color="white")

# Image ne save karvu
qr_img.save("qr_code.png")

print("QR Code successfully generated and saved as 'qr_code.png'.")
