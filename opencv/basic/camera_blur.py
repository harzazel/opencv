import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    blur = cv2.GaussianBlur(frame,(25,25),0)

    # Display the resulting frame
    cv2.imshow('frame', blur)

    # ESC to exit
    k = cv2.waitKey(10)
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()