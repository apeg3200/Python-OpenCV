import cv2
import numpy as np
import pylibdmtx.pylibdmtx

e1 = cv2.getTickCount()

ori = cv2.imread('Calculadora.jpg', 1)

# cv2.namedWindow('space', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('space', 800, 500)

gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)

_, image = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
# image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

(_, cnts, _) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(ori, [box], -1, (0, 255, 0), 10)

data_matrix1 = ori[777:989, 829:1037]
data_matrix2 = ori[2200:2470, 3300:3570]

result = pylibdmtx.pylibdmtx.decode(data_matrix1)
if result:
    print("Data matrix encontrados:")
    print(result)
result = pylibdmtx.pylibdmtx.decode(data_matrix2)
if result:
    print(result)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

# cv2.imshow('space', data_matrix1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
