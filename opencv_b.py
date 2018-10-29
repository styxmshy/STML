# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:29:05 2018
用鼠标画图，m键切换，if True, draw rectangle. false,draw circle
@author: ccc solar okokok
"""

import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):#创建一个回调函数
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:#左键按下返回起始位置坐标
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:#左键按下画图，
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:#左键松开不画图，
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)
#和opencv主窗口绑定
#connect with the main opencv windows            
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image2')
cv.setMouseCallback('image2',draw_circle)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF    
    if k ==ord('m'):# m button
        mode=not mode 
    elif k==27:#esc button
        break
cv.destroyAllWindows()