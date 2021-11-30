import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
im = cv.imread('lena.jpg',0)
hist = cv.calcHist([im], [0], None, [256], [0, 256])
row, col = im.shape
type_image = [0, 0, 0]
for i in range(len(hist)):
     if i <= 85:
         type_image[0] += hist[i]
     elif i <= 170:
         type_image[1] += hist[i]
     else:
         type_image[2] += hist[i]
result = "Dark image" if type_image[0] > type_image[1] and type_image[0] > type_image[
     2] else "Low contrast" if type_image[1] > type_image[0] and type_image[1] > type_image[2] else "Bright image"
cv.imshow(f"this Image is : {result}", im)
cv.waitKey(0)