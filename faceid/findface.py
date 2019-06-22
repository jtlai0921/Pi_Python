from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import config


camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1024, 768))

time.sleep(1)


faceCascade = cv2.CascadeClassifier(config.HAAR_FACES)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):


    image = frame.array
    

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = config.HAAR_SCALE_FACTOR,
        minNeighbors = config.HAAR_MIN_NEIGHBORS,
        minSize = config.HAAR_MIN_SIZE,
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

    cv2.imshow('Video', image)
    

    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
