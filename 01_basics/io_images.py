import os 
import cv2


image_path = os.path.join('YOUR PATH') 


img = cv2.imread(image_path)


cv2.imwrite(os.path.join('.','data','download_out.jpg'), img)


cv2.imshow('image',img)
cv2.waitKey(5000)
