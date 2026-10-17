import os
import cv2


img = cv2.imread(os.path.join('.' , 'data' , 'download.jpg'))
print(img.shape)
cv2.imshow('img',img)
cv2.waitKey(0)


cropped_img = img[320:640, 420:840]
print(cropped_img.shape)
cv2.imshow('croped_img',cropped_img)
cv2.waitKey(0)
