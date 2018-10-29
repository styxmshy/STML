# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:07:29 2018

@author: styxm
"""
#Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('d:\st.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()