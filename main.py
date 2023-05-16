from  __future__ import print_function
import numpy as np
import cv2
import os
import time

cap = cv2.VideoCapture(0)

fonte = cv2.FONT_HERSHEY_TRIPLEX
fonte_ = cv2.FONT_HERSHEY_COMPLEX

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,minSize=(50, 50), maxSize=None)
    cv2.rectangle(frame, (0, 0), (800, 45), (40, 40, 40), -2)

    if len(faces) > 0:
	
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x - 10, y - 20), (x + w + 10, y + h + 10), (0, 255, 255), 2)
            roi_gray = frame[y-15:y + h+10, x-10:x + w+10]
            cv2.putText (frame, 'Person found!', (175, 32), fonte_, 1, (255, 255, 255), 2)

    else:
        cv2.putText (frame, 'Searching...', (200, 32), fonte_, 1, (255, 255, 255), 2)

    # cv2.putText (frame, "II Setic - IFC - Campus SBS", (150, 465), fonte, 2, (0, 0, 0), 10)
    # cv2.putText (frame, "II Setic - IFC - Campus SBS", (150, 465), fonte, 2, (0, 255, 0), 2)
    cv2.namedWindow("Face Detection", 2)
    cv2.setWindowProperty("Face Detection", cv2.WND_PROP_FULLSCREEN, 1)
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
