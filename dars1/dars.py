import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
m=qrcode.QRCode(version=1,box_size=15,border=5)
m.