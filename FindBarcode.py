import cv2
import pylibdmtx.pylibdmtx
from PIL import Image
import pyzbar.pyzbar
import numpy as np

image = cv2.imread('calc2.jpg')

# procura por código de barras ou QR Code
# result = pyzbar.pyzbar.decode(image)
# if result:
#     print("Códigos de barras e QR Codes encontrados:")
#     print(result)


# procura por data matrix
result = pylibdmtx.pylibdmtx.decode(image)
if result:
    print("Data matrix encontrados:")
    print(result)
