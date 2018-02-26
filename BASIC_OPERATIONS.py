import numpy as np
import cv2

img = cv2.imread("barcode.jpg", 1)
# px = img[200, 200]

i = 0
while i < 200:
    img[i, i] = [0, 255, 0]
    i += 1

cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()