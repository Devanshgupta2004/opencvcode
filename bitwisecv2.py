import cv2
import numpy as np

img=cv2.imread("im.jpg")
img1=np.zeros(img.shape,np.uint8)
img2=np.ones(img.shape,np.uint8)

cv2.rectangle(img1,(50,50),(300,300),(123,213,213),-1)
cv2.circle(img2,(123,123),100,(234,234,234),-1)
#bitwise operation for masking

img3=cv2.bitwise_and(img1,img2)
cv2.imshow("f1",img)
cv2.imshow("f2",img1)
cv2.imshow("f3",img3)
cv2.waitKey()
cv2.destroyAllWindows()
 