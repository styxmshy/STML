# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:36:24 2018

@author: styxm
"""

import numpy as np
import cv2 as cv
# read the video file 
cap = cv.VideoCapture('d:\output.avi')#

while(cap.isOpened()):
    #ret(true or false:indicates whether the frame has been read )
    #frame(indicates currently read frame)
    ret, frame = cap.read()
    # judge if have a frame
    if ret == True:
       frame=cv.flip(frame,0)#frame flip
       
       gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #frame BGR transfer gray   
       
       cv.imshow('frame',gray)
    else:
        break

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()