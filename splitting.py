import cv2

image = cv2.imread('barcode.jpg', 1)
b, g, r = cv2.split(image)
image[:, 2, :] = 255
cv2.imshow('win', image)
cv2.waitKey(0)
cv2.destroyAllWindows()