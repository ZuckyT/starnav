from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import math

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
thresh = cv2.threshold(blurred, 175, 255, cv2.THRESH_BINARY) [1]
labels = measure.label(thresh, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
print("Mask: ", mask)
np.savetxt('mask.txt', mask, delimiter=',')
for label in np.unique(labels):
	print("Label: ", label)
	if label==0:
		continue
	labelMask = np.zeros(thresh.shape, dtype="uint8")
	labelMask[labels == label] = 255
	numPixels = cv2.countNonZero(labelMask)
	if numPixels > 3:
		mask = cv2.add(mask, labelMask)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = contours.sort_contours(cnts) [0]
class pos:
	def __init__(self, x, y):
		self.x = x
		self.y = y

posArray  = []
k=0
for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)
	((cX, cY), radius) = cv2.minEnclosingCircle(c)
	print(x, y)
	coord = pos(x, y)
	posArray.append(coord)
	k=k+1
	cv2.circle(image, (int(cX), int(cY)), int(radius), (0, 0, 255), 3)
	cv2.putText(image, "#{}".format(i+1), (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, .45, (0, 0, 255), 2)
for obj in posArray:
	print(obj.x, obj.y, sep =' ')
xD = abs(posArray[0].x-posArray[1].x)
yD = abs(posArray[0].y-posArray[1].y)
distance = math.sqrt((xD*xD)+(yD*yD))
print("xD: ", xD, " yD: ", yD, " Distance: ", distance)
path = '/home/brynm/sf2022/cStar/image.png'
cv2.imwrite('image.png', image)
#cv2.imshow("Image", image)
#cv2.waitKey(0)
