import numpy as np
import cv2

# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("barcode.jpg", 1)
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img, (180,130),(423,300),(0,255,0),5, cv2.LINE_AA)
img = cv2.circle(img, (290,211), 60, (255,0,0), 10)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[200,20],[500,3600]], np.int32)
img = cv2.polylines(img, [pts], True, (0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Alan', (200,400), font, 4, (255,255,255),2,cv2.LINE_AA)
cv2.putText()
cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()