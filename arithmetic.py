import numpy as np
import cv2

img1 = cv2.imread('dedo.png', 1)
img2 = cv2.imread('dedo2.png', 1)

added = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('window', added)
cv2.waitKey(0)
cv2.destroyAllWindows()