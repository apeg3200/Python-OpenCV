import cv2
import numpy as np

#Faz a diferença entre a dilation e a erosion da imagem
#basicamente produz os contornos de uma imagem

image = cv2.imread('j.png', 0)
kernel = np.ones((3, 3), np.uint8)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('window', image)
cv2.imshow('window2', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
