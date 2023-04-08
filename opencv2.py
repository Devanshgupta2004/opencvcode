#take photo automatic
import cv2

image =cv2.VideoCapture(0)#may be 1 and -1
#to make video
fourcc_code=cv2.VideoWriter_fourcc(*"XVID")
video=cv2.VideoWriter("my .avi",fourcc_code,30,(480,640,10))
#open the camrea put loop to take many
while(True): 
    check,frame=image.read()
    video.write(frame)
    cv2.imshow("im",frame)
    if cv2.waitKey(1) == ord("q"):
        break

    print(frame.shape)

#to save iamge on camera
    cv2.imwrite("im.jpg",frame)

#shut the cameer
video.release()
image.release()

cv2.destroyAllWindows()
###end


