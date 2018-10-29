# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:44:51 2018

@author: styxm
"""
import numpy as np
import cv2

img = cv2.imread('d:\st.jpg')

#画绿色矩形,以后是程序检测到眼睛画框
green = (0,255,0)
cv2.rectangle(img,(100,80),(380,380),green)
cv2.imshow("img",img)
cv2.waitKey(0)

cv2.imshow('img',img)
cv2.waitKey(0)
sp = img.shape
print(sp)
sz1 = sp[0]#height(rows) of image
sz2 = sp[1]#width(colums) of image
sz3 = sp[2]#the pixels value is made up of three primary colors
print ('width: %d \nheight: %d \nnumber: %d' %(sz1,sz2,sz3))

im2 = cv2.resize(img, (430,430), interpolation=cv2.INTER_CUBIC)
for i in range(0,2):
    radius = np.random.randint(5,high = 200)#生成1个[5,200)的随机数
    color = np.random.randint(0,high = 256,size = (3,)).tolist()#生成3个[0,256)的随机数
    pt = np.random.randint(0,high = 300,size = (2,))#生成2个[0,300)的随机数
    cv2.circle(im2,tuple(pt),radius,color,-1)#画圆

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(im2,'shutong',(150,30), font, 1,(255,255,255),1,cv2.LINE_AA)

cv2.imshow('img2',im2)

sp = im2.shape
print(sp)
sz11 = sp[0]#height(rows) of image
sz21 = sp[1]#width(colums) of image
sz31 = sp[2]#the pixels value is made up of three primary colors
print ('width: %d \nheight: %d \nnumber: %d' %(sz11,sz21,sz31))
cv2.waitKey(0)
cv2.destroyAllWindows()
