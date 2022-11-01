import cv2 as cv
import numpy as np

image =cv.imread("dog.jpg",0)
cv.imshow("original",image)
Height = image.shape[0]
Width = image.shape[1]
invIm = np.zeros([Height, Width], dtype=np.uint8)
for i in range(Height):
    for j in range(Width):
        invIm[i, j] = 255 - image[i, j]


cv.imshow("invented",invIm)

cv.waitKey()