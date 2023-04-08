import cv2
import numpy as np

img = cv2.imread("im.jpg")
img3=cv2.imread("19-00-12-Z.jpg")
image3=np.ones(img.shape,np.uint8)
image3=image3*100
img3=cv2.resize(img3,(512,512))
img=cv2.resize(img,(512,512))
img5=cv2.addWeighted(img,0.7,img3,0.3,0)#put ) at % postion


# img2=cv2.add(img,image3)

cv2.imshow("asd",img)
# cv2.imshow("asd3",img2)
cv2.imshow("asd09",img5)
cv2.waitKey()
cv2.destroyAllWindows()

#to add two image use resize to make size same and 
#to give proiraty use cv2.addWeighted(image)