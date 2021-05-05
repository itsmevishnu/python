import cv2
import numpy as np
# import dlib

#capturing the video
capture  = cv2.VideoCapture(0)
#detect the faces
#detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # faces = detector(gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord(q):
       break

capture.release()
cv2.destroyAllWindows()
