# 轮廓识别
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


src = cv.imread("1.png")
cv.imshow("original", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (3, 3), 0)
ret, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
copy_img = src.copy()
cv.drawContours(copy_img, contours, -1, (255, 0, 0), 2)
cv.imshow("contours", copy_img)
print(len(contours))

cv.waitKey(0)
cv.destroyAllWindows()
