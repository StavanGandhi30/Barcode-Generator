from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open(path))
value = str(data[0][0])
output = value.replace("b'","").replace("'","")
print(output)
