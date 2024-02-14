# import qrcode as qr

# img = qr.make("https://peraan.in/")
# img.save("QR.png")


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('www.peraan.in/')
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR1.png")