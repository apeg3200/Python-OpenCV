import cv2
import numpy as np
from matplotlib import pyplot as plt

# using open cv calcHist method

img = cv2.imread('barcode.jpg', 0)
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.show()

#using matplotlib

img = cv2.imread('barcode.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

#histogram equalization

img = cv2.imread('barcode.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ)) #stacking images side-by-side
cv2.imshow('res.png', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#CLAHE adaptative histogram equalization

img = cv2.imread('barcode.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
res_clahe = np.hstack((img, cl1))
cv2.imshow('clahe_2.jpg', res_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()
