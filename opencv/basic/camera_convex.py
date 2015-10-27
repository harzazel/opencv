import cv2                             
import numpy as np

cap = cv2.VideoCapture(0) 
while(cap.isOpened()) :
	ret, frame  = cap.read()

	imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,127,255,0)

	img_contour, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	max_area = 0
	if len(contours) > 0:
		for i in range(len(contours)):
			cnt=contours[i]
			area = cv2.contourArea(cnt)
			if(area>max_area):
				max_area=area
				ci=i
		cnt = contours[ci]
		hull = cv2.convexHull(cnt)

		drawing = np.zeros(frame.shape,np.uint8)
		cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
		cv2.drawContours(drawing,[hull],0,(0,0,255),2)

		cv2.imshow('picture', drawing)

	k = cv2.waitKey(10)
	if k == 27:
		break