from rembg import remove
from PIL import Image
input_path = 'name.jpg'
output_path = 'newname.jpg'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)