# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 12:05:20 2018

@author: styxm
"""

import numpy as np
import cv2 as cv
img = cv.imread('d:\st.jpg',0)
cv.namedWindow('image',cv.WINDOW_NORMAL)#可以调整图像窗口大小
cv.imshow('image',img)

k = cv.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('d:\st1.png',img)
    cv.destroyAllWindows()
    