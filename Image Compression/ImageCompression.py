import PIL.Image
from tkinter.filedialog import *
img = PIL.Image.open("69936.jpg")
img.save("new.jpg","JPEG",optimize=True,quality=10)
PIL.Image.open("new.jpg")