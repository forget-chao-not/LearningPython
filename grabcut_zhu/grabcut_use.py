import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('E:/Image/zhu.jpg')

#plt.imshow(img)

mask= np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (0,120 ,420,533)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
dst=img*mask2[:,:,np.newaxis]
cv2.imshow('dst',dst)

img2=cv2.imread('E:/Image/data/starry_night.jpg')
cv2.imshow('img2',img2)

roi_zhu=dst[160:533,0:430]
cv2.imshow('roi_zhu',roi_zhu)
roi_2=img2[227:600,0:430]
cv2.imshow('roi_2',roi_2)

kernel=np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(roi_zhu,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)

##kernel2 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
##sharp=cv2.filter2D(opening,-1,kernel2)
##cv2.imshow('sharp',sharp)
bilateral= cv2.bilateralFilter(opening,5,75,75)
cv2.imshow('bilateral',bilateral)
cv2.imwrite('E:/Image/pig.jpg',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
