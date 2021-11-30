import numpy as np
import cv2

image = cv2.imread('chest_xray.jpg')

print("1. brighten")
print("2. reduce brightness")
brightness = int(input("Enter Brightness: "))


if brightness == 1:
    level = input("Enter level-- low/medium/high : ")
    if level == 'low':
        gamma04 = np.array(255*(image/255)**0.67,dtype='uint8')
    elif level == 'medium':
        gamma04 = np.array(255*(image/255)**0.2,dtype='uint8')
    elif level == 'high':
        gamma04 = np.array(255*(image/255)**0.04,dtype='uint8')
elif brightness == 2:
    level = input("Enter level-- low/medium/high : ")
    if level == 'low':
        gamma04 = np.array(255*(image/255)**1.5,dtype='uint8')
    elif level == 'medium':
        gamma04 = np.array(255*(image/255)**5,dtype='uint8')
    elif level == 'high':
        gamma04 = np.array(255*(image/255)**25,dtype='uint8')

image2 = cv2.hconcat([image,gamma04])
cv2.imshow('gamma transformation',image2)

cv2.waitKey(0)