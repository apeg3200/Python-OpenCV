import cv2
import numpy as np


img = cv2.imread('bars.jpg', 0)
# edges = cv2.Canny(img, 50, 50)
_, contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# child = [hierarchy[0][i][:] for i in range(len(contours)) if hierarchy[0][i][3] == -1]

print("Contours\n")
# print(contours)
print("Hierarchy\n")
print(hierarchy)
