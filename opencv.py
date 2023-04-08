# to open image
import cv2

image=cv2.imread("E:\pkgmobilegalery1-1-2020/19-00-12-Z.jpg")
cv2.imshow("f",image)
cv2.waitKey()
cv2.destroyAllWindows()

#to give image size(lenght,berath,color used)
print(image.shape)
#use to not call full address
cv2.imwrite("19-00-12-Z.jpg",image)
image=cv2.imread("./19-00-12-Z.jpg")
cv2.imshow("f",image)
cv2.waitKey()
cv2.destroyAllWindows()

#to makeblack and white cv2.
grey_f=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("f",grey_f)
cv2.waitKey()
cv2.destroyAllWindows()

#to merge diffrent color use 
B,R,G=cv2.split(image)
merge=cv2.merge([B,R,G+244])
cv2.imshow("f",merge)
cv2.waitKey()
cv2.destroyAllWindows()
