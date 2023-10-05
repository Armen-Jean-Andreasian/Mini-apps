"""
1. Download (and install) tesseract-ocr from https://github.com/UB-Mannheim/tesseract/wiki
    Gonna be installed by C:/Users/pc/AppData/Local/Programs/Tesseract-OCR

2. pip install tesseract
"""

import pytesseract
from PIL import Image


class ImageReader:
    path_tesseract = r'E:\Users\pc\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = path_tesseract

    @staticmethod
    def convert(image_path_):
        img = Image.open(image_path_)
        text = pytesseract.image_to_string(img)
        return text


image_path = 'image.png'
result = ImageReader.convert(image_path_=image_path)
print(result)

# however, at this version of tesseract is weak.
