import cv2
import numpy as np
from matplotlib import pyplot as plt

#Canny é um algoritmo de detecção de bordas.
#param 1 é a imagem
#param 2 é o minVal
#param 3 é o maxVal

e1 = cv2.getTickCount()

img2 = cv2.imread('iwl.png', 1)
img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img = cv2.blur(img, (3, 3))
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow('s', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
edges = cv2.Canny(img, 50, 50)



_, countours_ex, hierarchy_ex = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_, countours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

loop = 0
out = np.zeros_like(img3)  # Extract out the object and place into output image
holes = [countours[i] for i in range(len(countours)) if hierarchy[0][i][3] == -1]

print(countours.__len__())
print(holes.__len__())

for c in holes:
    c = sorted(holes, key=cv2.contourArea, reverse=True)[loop]
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    if cv2.contourArea(box) > 1000:
        #aproxima a curva pelo algoritmo Douglas-Peucker
        # epsilon = 0.1 * cv2.arcLength(cnt, True)
        # approx = cv2.approxPolyDP(cnt, epsilon, True)

        #aproxima curva do contorno
        approx = cv2.convexHull(c)
        cv2.drawContours(img2, [approx], -1, (255, 0, 0), 1)
        loop = loop + 1

        #extrai images cortadas para análise
        mask2 = np.ones_like(img3)  # Create mask where white is what we want, black otherwise
        cv2.drawContours(mask2, [approx], -1, 255, -1)  # Draw filled contour in mask
        out[mask2 == 255] = img3[mask2 == 255]

        print(cv2.contourArea(box))

print(loop)
mask = np.zeros_like(edges)
cv2.drawContours(mask, [approx], -1, (255, 0, 0), 1)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

# cv2.imshow('img', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
output = cv2.cvtColor(out, cv2.COLOR_GRAY2RGB)

plt.subplot(121), plt.imshow(edges, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(output, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

plt.show()
