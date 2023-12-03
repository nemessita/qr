import qrcode as qr
img = qr.make("A1+A2")
img.save("test.png")