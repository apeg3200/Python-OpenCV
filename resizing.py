import cv2

cv2.namedWindow('space', cv2.WINDOW_NORMAL)
cv2.resizeWindow('space', 800, 600)

im = cv2.imread('Calculadora2.jpg')
# h, w = im.shape[:2]
# im = cv2.resize(im, (2*w, 2*h), interpolation=cv2.INTER_AREA)

cv2.imshow('space', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
