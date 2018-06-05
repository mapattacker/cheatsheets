# Object Character Recognition
import pytesseract
from PIL import Image
import os

# to install pytesseract
    # Mac 'brew install tesseract'
    # Ubuntu 'sudo apt-get install tesseract-ocr'


# screenshot & open image
os.system('screenshot screen.png')
img = Image.open('screen.png')

# crop image
area = (400, 400, 800, 800)
cropped_img = img.crop(area)
# cropped_img.show()

# OCR
text = pytesseract.image_to_string(img)
print(text)