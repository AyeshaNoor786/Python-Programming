from PIL import Image

img = Image.open("image.jpg")
blackwhite = img.convert("L")
blackwhite.save('bw_image.jpg')
blackwhite.show()