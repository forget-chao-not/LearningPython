##寻找绿色的物体

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

##img=cv2.imread('E:/Image/baby.jpg',cv2.IMREAD_COLOR)
##
##img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
##
##plt.imshow(img)
##plt.show()


capture=cv.VideoCapture(0)
while True:
    ret,frame=capture.read()
    cv.imshow('demo',frame)

    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_hsv=np.array([37,43,46])
    upper_hsv=np.array([77,255,255])
    mask=cv.inRange(hsv,lower_hsv,upper_hsv)
    dst=cv.bitwise_and(frame,frame,mask=mask)
    
    cv.imshow('mask',dst)

    
    c=cv.waitKey(30)
    if c==27:
        break

capture.release()
cv.destroyAllWindows()

print('哈哈')
