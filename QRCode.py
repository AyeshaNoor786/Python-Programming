import qrcode
 
data = 'Enter your data'
img = qrcode.make(data)
 
img.save('QRCode.png')