import numpy as np
import cv2
import time
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')




while True:
    ret, frame = cap.read()

    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(255,0,0),5)
        roi_gray = gray[y:y+w, x:x+w ]
        roi_color = frame[y:y+h, x:x+w]

    # eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
    # for (ex,ey,eh,eh) in eyes:
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)


    cv2.imshow('frame', frame)

    if len(faces):
        time.sleep(3)
        showPic = cv2.imwrite(os.path.join('./images/','filename.jpg'),frame)
        break
    else:
        print("no face")
   
    # if ret:
    #     print("success")
    #     cv2.imshow('frame',frame)
    # else:
    #     break
    if cv2.waitKey(1) == ord('q'):
        showPic = cv2.imwrite("filename.jpg",frame)
        break

cap.release()
cv2.destroyAllWindows()