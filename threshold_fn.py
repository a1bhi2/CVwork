# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:53:46 2018

@author: Abhishek
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("lion.jpg",0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('lion',img)
cv2.imshow('atM',th2)
cv2.imshow('atg',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(thresh1) 