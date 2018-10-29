# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:03:30 2018

@author: styxm
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('d:\st.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()