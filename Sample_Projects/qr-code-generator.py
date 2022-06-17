import qrcode 
data = "This QR belongs to Amit"
img = qrcode.make(data)
img.save("/home/amit/Documents/myqrcose.png")