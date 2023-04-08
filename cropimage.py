import numpy as np
import cv2

def mouse_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if len(points)==2:
            cv2.rectangle(img,points[0],points[1],(0,255,23),3)
            #get the crop image to save use cv2.imwrite
            crop_image=img[points[-2][1]:points[-1][1],points[-2][0]:points[-1][0]]
            cv2.imshow("frame1",crop_image)
    # to create line when mouse move
    # if event==cv2.EVENT_MOUSEMOVE:
    #     points.append((x,y))
    #     if len(points)>=2:
    #         cv2.line(img,points[-2],points[-1],(13,45,78),5)
    # cv2.imshow("frame",img)
img = cv2.imread("im.jpg")
points=[]
cv2.imshow("frame",img)
#to operate mouse
cv2.setMouseCallback("frame",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
