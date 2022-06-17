import qrcode 
data = "This QR belongs to Amit"
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fil_color = 'red', back_color = 'white')

img.save("/home/amit/Documents/myqrcode-custom.png")