import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 60, (0,255,0), 10)

img = cv2.imread('barcode_mj.jpg', 1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0XFF == 27:
        break
cv2.destroyAllWindows()