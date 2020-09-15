
# 相似图片识别
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img_rgb = cv.imread("22.jpeg")
template = cv.imread("2332.jpg", 0)
cv.imshow("original", img_rgb)
img_grey = cv.cvtColor(img_rgb,cv.COLOR_BGR2GRAY)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_grey, template, cv.TM_CCOEFF_NORMED)
th = 0.6
loc = np.where( res >= th)

for pt in zip(*loc[::-1]): 
  cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)


copy_img = img_rgb.copy()
cv.imshow("contours", copy_img)

cv.waitKey(0)
cv.destroyAllWindows()
