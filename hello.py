#!/usr/bin/env python
#import cv2
#import numpy as np


#img = cv2.imread('djames.png')
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

from  __future__ import print_function
import numpy as np
import cv2
import os
import time

cap = cv2.VideoCapture(0)

fonte = cv2.FONT_HERSHEY_TRIPLEX
fonte_ = cv2.FONT_HERSHEY_COMPLEX

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

fullscreen_WND = cv2.WND_PROP_FULLSCREEN

while (cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,minSize=(50, 50), maxSize=None)
    cv2.rectangle(frame, (0, 0), (800, 45), (40, 40, 40), -2)

    if len(faces) > 0:
	
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x - 10, y - 20), (x + w + 10, y + h + 10), (0, 255, 255), 2)
            roi_gray = frame[y-15:y + h+10, x-10:x + w+10]
            cv2.putText (frame, 'Pessoa detectada!', (175, 32), fonte_, 1, (255, 255, 255), 2)

    else:
        cv2.putText (frame, 'Procurando...', (200, 32), fonte_, 1, (255, 255, 255), 2)

    cv2.putText (frame, "III Setic", (150, 465), fonte, 2, (0, 0, 0), 10)
    cv2.putText (frame, "III Setic", (150, 465), fonte, 2, (0, 255, 0), 2)
    cv2.namedWindow("III Setic", 2)
    cv2.setWindowProperty("III Setic", cv2.WND_PROP_FULLSCREEN, 1)
    cv2.imshow("III Setic", frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
