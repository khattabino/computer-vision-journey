import os
import cv2



img = cv2.imread(os.path.join('.','data','download.jpg'))

print(img.shape)

img_line = cv2.line(img, (100, 150) , (300, 450) , (0,255,0) ,10) 
img_rec = cv2.rectangle(img, (100, 150) , (300, 450) , (0,255,0) ,10) 
img_circle = cv2.circle(img, (150,200) , 200 , (0,255,0) ,10) 
img_text = cv2.putText(img, 'hey you!', (150,250),cv2.FONT_HERSHEY_SIMPLEX,2, (255,255,0), 2) 























cv2.imshow('img', img)
cv2.waitKey(0)