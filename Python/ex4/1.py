import cv2
import numpy as np
import matplotlib.pyplot as plt

tt = int(input("ความสว่าง: "))
img = cv2.imread('lena2.jpg',0)

plt.hist(img.ravel(), tt, (0, 256))
plt.show()