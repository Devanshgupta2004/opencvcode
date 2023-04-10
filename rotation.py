import cv2
import numpy as np

img=cv2.imread("im.jpg")
row,col,ch=img.shape
#animation
angle=0
while(True):

    R=cv2.getRotationMatrix2D((row/2,col/2),angle,.8)
    img2=cv2.warpAffine(img,R,(col,row))

    cv2.imshow('f1',img)
    cv2.imshow('f2',img2)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    angle=angle+1
cv2.destroyAllWindows()