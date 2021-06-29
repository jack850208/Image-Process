# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:08:52 2021

@author: AIC
"""
import numpy as np
import cv2 as cv

fig_img = cv.imread(r'fig.png')
imgray = cv.cvtColor(fig_img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)


cv.imshow('win', thresh)
cv.waitKey(0)
cv.imshow('win', imgray)
cv.waitKey(0)
cv.destroyAllWindows()