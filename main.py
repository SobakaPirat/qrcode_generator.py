import qrcode
qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)

data = input("please, write your text for QRCode here:")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("1.pngpython")