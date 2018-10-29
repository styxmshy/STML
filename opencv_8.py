# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:19:11 2018

@author: styxm
"""

import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")

#画绿线
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green,2)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画红线
red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)
cv2.imshow("Canvas",canvas)  
cv2.waitKey(0)
#画绿色矩形
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画红色矩形
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画蓝色矩形
blue = (255,0,0,)
cv2.rectangle(canvas,(200,50),(225,125),blue,-1)#-1表示实心
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画圆1——有规律的画圆
canvas = np.zeros((300,300,3),dtype="uint8")#重新初始化变量canvas(三维的矩阵)
(centerX,centerY) = (canvas.shape[1] // 2,canvas.shape[0] // 2)#获取图像中心
white = (255,255,255)#设置白色变量
for r in range(0,175,25):
    cv2.circle(canvas,(centerX,centerY),r,white)#circle(图像，圆心，半径，颜色)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
#画圆2——随机画圆
for i in range(0,25):
    radius = np.random.randint(5,high = 200)#生成1个[5,200)的随机数
    color = np.random.randint(0,high = 256,size = (3,)).tolist()#生成3个[0,256)的随机数
    pt = np.random.randint(0,high = 300,size = (2,))#生成2个[0,300)的随机数
    cv2.circle(canvas,tuple(pt),radius,color,-1)#画圆
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
