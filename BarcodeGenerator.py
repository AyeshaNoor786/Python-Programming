import barcode
from barcode.writer import ImageWriter

number=input("Enter the code to generate barcode: ")
barcode_format = barcode.get_barcode_class('upc')
mybarcode = barcode_format(number,writer=ImageWriter())
mybarcode.save("Barcode")