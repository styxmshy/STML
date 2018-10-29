import tensorflow as tf
import cv2 
img=cv2.imread('d:\st.jpg',0)
cv2.namedWindow('st',cv2.WINDOW_NORMAL)#可以调整图像窗口大小
cv2.imshow('st',img)
cv2.imwrite('mes.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()