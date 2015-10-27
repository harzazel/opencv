import numpy as np
import cv2

cap = cv2.VideoCapture(0)
LINE_RGB = (0,255,0)
LINE_WIDTH = 1
TRESHOLD_VALUE = 127
TRESHOLD_MAX = 255

while(cap.isOpened()):
    ret, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (25, 25), 0, 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
    thresh = cv2.adaptiveThreshold(gray, TRESHOLD_MAX, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, LINE_RGB, LINE_WIDTH)

    # Display the resulting frame
    cv2.imshow('contours', frame)
    cv2.imshow('picture', image)

    # ESC to exit
    k = cv2.waitKey(10)
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()