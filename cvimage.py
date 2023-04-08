import numpy as np
import cv2

#shape making with(lenght,breath,side).type
img1=np.zeros((512,512,3),np.uint8)
img=cv2.imread("im.jpg")
print(img.shape)

#to crate line

#to filed with color use -1 at last
cv2.line(img,(10,10),(155,155),(13,45,78),5)
#to create arrow line
cv2.arrowedLine(img1,(15,30),(118,199),(123,32,213),10)
cv2.rectangle(img,(12,234),(123,122),(12,12,132),4)

#to put text in shape
cv2.putText(img,"Devansh",(200,200),cv2.FONT_HERSHEY_SIMPLEX,3,(12,123,23),3)

cv2.imshow("dfshape",img)
cv2.imshow("shape",img1)
cv2.waitKey()
cv2.destroyAllWindows()

