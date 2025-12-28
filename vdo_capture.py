import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # ret :- tells capture is working properly
    # frame :- nparray representing img
    ret, frame = cap.read()

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
