import cv2

def mouse_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img,"Devansh",(x,y),cv2.FONT_HERSHEY_SIMPLEX,3,(12,123,23),3)
    cv2.imshow("frame",img)
    # to create line when mouse move
    if event==cv2.EVENT_MOUSEMOVE:
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-2],points[-1],(13,45,78),5)
    cv2.imshow("frame",img)
img = cv2.imread("im.jpg")
points=[]
cv2.imshow("frame",img)
#to operate mouse
cv2.setMouseCallback("frame",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
