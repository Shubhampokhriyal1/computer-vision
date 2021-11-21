import cv2

#chanel order is BGR color 
image =cv2.imread('test.png',cv2.IMREAD_UNCHANGED)# read iamge ('image name', cv2.instance)

#function to display img

cv2.imshow('Test Image',image) #function to show image 
cv2.waitKey()  #wait until any key is pressed or pass argument(3000ms)
