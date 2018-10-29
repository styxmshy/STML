# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:21:08 2018

@author: styxm
"""

import numpy as np
import cv2 as cv

# read the capture of the notebook camera (number 0)
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  
    #ret(true or false:indicates whether the frame has been read )
    #frame(indicates currently read frame)
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',gray)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()