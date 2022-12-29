from rembg import remove
from PIL import Image
input_path = "With_background.jpg"
output_path = "without_background.jpeg"
inp = Image.open(input_path)
output = remove(inp)
rgb_im = output.convert('RGB')
rgb_im.save(output_path)