import cv2

logo = cv2.imread('logo_cut2.jpg', -1)
ret, mask = cv2.threshold(logo, 10, 255, cv2.THRESH_BINARY)
baw = cv2.bitwise_not(mask)

cv2.imwrite('log.png', baw)
cv2.waitKey(0)
cv2.destroyAllWindows()