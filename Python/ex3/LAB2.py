import numpy as np
import cv2
img = cv2.imread("low1.jpg")
xp = [0, 120, 180, 255]
fp = [0, 50, 220, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
result = cv2.LUT(img, table)
img3 = cv2.hconcat([img,result])
cv2.imshow('gamma transformation',img3)
cv2.waitKey(0)