##pip install python-barcode

import barcode
from barcode.writer import ImageWriter
barcode = barcode.get('Code39', '08302004', writer=ImageWriter())
save = barcode.save('barcode')
