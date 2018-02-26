import cv2

img = cv2.imread('barcode.jpg', 1)
dedo = img[300:450, 0:150]
img[0:150, 0:150] = dedo
img = cv2.line(img, (0, 0), (600, 450), (0, 255, 0), 5)
img = cv2.line(img, (600, 0), (0, 450), (0, 255, 0), 5)
cv2.imwrite('dedo.png', dedo)


print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()