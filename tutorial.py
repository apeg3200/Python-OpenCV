import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("dedo.png", 1)
img = cv2.rectangle(img, (0, 0), (150,150), (250, 255, 0), 70)
# img = cv2.circle(img, (290,211), 60, (255,0,0), 10)
cv2.imshow('window', img)
cv2.imwrite('dedo2.png', img)
cv2.waitKey(0)
# cv2.imwrite('barcode_mj.jpg', img)
cv2.destroyAllWindows()