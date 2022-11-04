import pyqrcode
from PIL import Image
import png
link = input("Enter anything to generate QR code : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=10)
Image.open("QRCode.png")