import cv2
import numpy as np

#Erosion avalia em cada pixel os pixels brancos na vizinhança. Caso sejam todos 1 (brancos) então o pixel
#permanece branco. Caso contrário, ele é apagado (preto).

image = cv2.imread('j.png', 0)
kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(image, kernel, iterations=3)

cv2.imshow('window', image)
cv2.imshow('window2', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
