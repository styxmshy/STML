# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:22:27 2018

@author: styxm
"""

import numpy as np
import cv2 as cv
# mouse callback function(double click)
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),50,(255,0,0),-1)
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:#esc button
        break
cv.destroyAllWindows()