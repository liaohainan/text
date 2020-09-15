
# 轮廓识别
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



im = cv.imread("3.png")
cv.imshow("original", im)
g = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
cv.imshow("original", g)
ret,th = cv.threshold(g,236,255,0)
cts, hi = cv.findContours(th,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# print(img)
print(len(cts)-1)
# print(hi)

for i in range(0,len(cts)): 
  x, y, w, h = cv.boundingRect(cts[i])  
  cv.rectangle(im, (x,y), (x+w,y+h), (0,0,100), 1)



# gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# gray = cv.GaussianBlur(gray, (3, 3), 0)
# ret, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
copy_img = im.copy()
cv.drawContours(copy_img, cts, -1, (255, 0, 0), 2)
cv.imshow("contours", copy_img)
print(len(contours))

cv.waitKey(0)
cv.destroyAllWindows()
