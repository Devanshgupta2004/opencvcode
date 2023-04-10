import cv2
import numpy as np

img=cv2.imread("im.jpg")
row,col,ch=img.shape
x=0
y=0

#for animation use loop
while(True):

#creating trasition matrix
    T=np.float64([[1,0,x],[0,1,y]])
#to shift
    img2=cv2.warpAffine(img,T,(col,row))
    cv2.imshow('f1',img)
    cv2.imshow('f2',img2)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    x=x+1
    y=y+1
cv2.destroyAllWindows()
