import cv2
import numpy as np

img=cv2.imread("im.jpg")
row,col,ch=img.shape
x=row/2
y=col/2

#creating trasition matrix
T=np.float64([[1,0,x],[0,1,y]])
#to shift
img2=cv2.warpAffine(img,T,(col,row))
cv2.imshow('f1',img)
cv2.imshow('f2',img2)
cv2.waitKey()
cv2.destroyAllWindows()
