"""递归照片2"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def recurPhoto(img, src, affMat, n):
    # 透视变换
    affImg = np.zeros(img.shape)
    affImg = cv.warpPerspective(img, affMat, (width, height))
    # cv.imshow("affImg", affImg)

    grayImg = cv.cvtColor(affImg, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(grayImg, 1, 255, cv.THRESH_BINARY)
    mask = cv.medianBlur(mask, 3)
    # cv.imshow("binary", mask)

    for i in range(0, height):
        for j in range(0, width):
            if not mask[i, j]:
                src[i, j] = img[i, j]
            else:
                src[i, j] = affImg[i, j]

    n -= 1
    if n == 0:
        cv.imshow("dst", src)
        # cv.imwrite("daitao.png", src)
    else:
        recurPhoto(img, src, affMat, n)



img = cv.imread("C:/Users/www/Desktop/daitao.jpg")
# img = cv.resize(img, (624, 832))
img = cv.resize(img, (832, 624))
cv.imshow("img", img)
plt.imshow(img)
height, width, mode = img.shape

srcMat = np.float32([[0, 0], [0, height - 1], [width - 1, height - 1], [width - 1, 0]])
# endMat = np.float32([[329, 269], [327, 413], [599, 445], [615, 272]]) # 韩文瑜
# endMat = np.float32([[258, 348], [255, 648], [463, 642], [483, 351]]) # 朱颖
# endMat = np.float32([[158, 434], [172, 675], [364, 707], [375, 460]]) # 郝婵娟
# endMat = np.float32([[309, 257], [301, 412], [458, 469], [475, 298]]) # 峰
endMat = np.float32([[225, 181], [236, 302], [426, 282], [424, 174]])  # 代涛
affMat = cv.getPerspectiveTransform(srcMat, endMat)

dst = np.zeros(img.shape, np.uint8)
recurPhoto(img, img, affMat, 6)
plt.show()
cv.waitKey(0)
