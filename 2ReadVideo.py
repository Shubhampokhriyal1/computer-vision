import cv2

cap=cv2.VideoCapture(0)#capture video with help of VideoCapture(sourse)<.......>0 will direct us to webcam of your PC 


opened=cap.isOpened()# this function return bool vale by checking that the video is opened or not

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  #height of video
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   #width of video
fps = cap.get(cv2.CAP_PROP_FPS)    #fps of video

print("frames are {}".format(fps))

if(opened):#opened is declared at the line 4  
	while (cap.isOpened()):#we will have to display every frame while the video is captured
		ret, frame=cap.read()#cap.read return a tuple (if the frame is present,frame to be displayed)
		if(ret==True):#if the frame is present or not  
			cv2.imshow('waname',frame)#displaying image with help of inshow
			if(cv2.waitKey(2)==27):#ascii for esc is 27
				break #end the loop 
