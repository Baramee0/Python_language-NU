import cv2
img1 = cv2.imread('lena2.jpg',0)
img2 = cv2.imread('lena2.png',0)
hist_img1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist_img2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
if metric_val == 1:
    print("ภาพเหมือนกัน , มีผลต่างเท่ากับ = ", metric_val)
else:
    print("ภาพต่างกัน , มีผลต่างเท่ากับ = ", metric_val)
