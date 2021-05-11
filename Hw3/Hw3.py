# -*- coding: utf-8 -*-
"""
Created on Sun May  9 03:20:41 2021

@author: USER
"""


import cv2 as cv
import numpy as np
    
src = cv.imread('eye.jpg')
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows /8, param1=100, param2=30, minRadius=30, maxRadius=100)

    
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(src, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(src, center, radius, (255, 0, 255), 3)

cv.imwrite('eye_circle.jpg', src)

