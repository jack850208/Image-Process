#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 01:03:03 2021

@author: jack850208
"""
#import numpy as np
import cv2 as cv


# load image
img = cv.imread(r"test/road.jpg")
 
# load marker image
marker = cv.imread(r"test/road_edit.jpg")

"""  
  fetch only mark pattern(pattern color in white)
from marker image
"""
# fetch marker

marker = cv.subtract(marker, img) # get marker by user draw
marker = cv.cvtColor(marker, cv.COLOR_BGR2GRAY) # convert marker to gray
ret, marker = cv.threshold(marker,50,255,cv.THRESH_BINARY)#let marke image only contain 0 or 255
fg = marker.copy() # marker's front image
bg = marker.copy() # marker's background image

# fetch background image in white 
bg[bg == 255] = 0
bg[fg == 0] = 255

"""  mark the marker in front image:
------ note -----------
    0 is mark as unknown region
   integer number denote as 'N':
     N > 0, N = 1, 2, 3, ......
     
"""
ret, marker = cv.connectedComponents(fg)
marker = cv.watershed(img,marker)

# mark the edge with user set color
img[marker == -1] = [0, 0, 255]

# write image to file
cv.imwrite('test/marker.jpeg', marker)
cv.imwrite('test/water.jpeg', img)
