import cv2
import numpy as np

#Delation avalia em cada pixel os pixels brancos na vizinhança. Caso ao menos um seja 1 (brancos) então o pixel
#é transformado para branco. Caso contrário, ele permanece 0 (preto).

image = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations=1)

cv2.imshow('window', image)
cv2.imshow('window2', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
