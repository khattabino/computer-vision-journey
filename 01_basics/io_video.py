import os 
import cv2


video_path=os.path.join('.','data','clip32.mp4')

video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read()


    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(25)
        
video.release()
cv2.destroyAllWindows()

    






