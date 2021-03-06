import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # ESC to exit
    k = cv2.waitKey(10)
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()