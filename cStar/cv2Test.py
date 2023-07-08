import numpy as np
import cv2 as cv

img  = cv.imread('rainbow.jpg')
img[100, 100] = [234, 45, 123]
print("Image Shape: ", img.shape)
print("200, 100", img[200, 100])
print("100, 200", img[100, 200])
print("0, 255, 255: ", img[100, 100, 0])
cv.imshow("Rainbow", img)
cv.waitKey(0)
