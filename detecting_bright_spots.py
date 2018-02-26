# import the necessary packages
# from imutils import contours
# import imutils
from skimage import measure
import numpy as np
import cv2

cv2.namedWindow('space', cv2.WINDOW_NORMAL)
cv2.resizeWindow('space', 800, 600)

# load the image, convert it to grayscale, and blur it
image = cv2.imread("Calculadora2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# threshold the image to reveal light regions in the
# blurred image
thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

# perform a series of erosions and dilations to remove
# any small blobs of noise from the thresholded image
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)

cv2.imshow('space', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# perform a connected component analysis on the thresholded
# image, then initialize a mask to store only the "large"
# components
labels = measure.label(thresh, neighbors=8, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")

(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(image, [box], -1, (0, 255, 0), 10)

