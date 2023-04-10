import cv2
import numpy as np
# the concept of interpolation in used
# Inter_linear  default
# inter_area    reducing
#inter_cubic    zooming

img=cv2.imread('ima.jpg')
img2=cv2.resize(img,None,1.5,1.5,cv2.INTER_LANCZOS4)


#pryamid method
img2=cv2.pyrUp("img")

cv2.imshow("f1",img2)
cv2.waitKey()
cv2.destroyAllWindows()
