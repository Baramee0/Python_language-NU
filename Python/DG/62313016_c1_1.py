import numpy as np
import cv2

image = cv2.imread('A1.png')
cv2.imshow("1.1",image)

resize_image = cv2.resize(image , None , fx=0.5, fy=0.5)
cv2.imshow("1.2",resize_image)

gamma = np.array(255*(resize_image/255)**0.2,dtype='uint8')
cv2.imshow("1.3",gamma)

gray = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('1.4',gray)

(thresh, BlackAndWhite) = cv2.threshold(resize_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("1.5",BlackAndWhite)



cv2.waitKey(0)