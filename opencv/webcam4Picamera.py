from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1024, 768))
time.sleep(1)
cascPath = 'haarcascade_frontalface_alt.xml'
if(len(sys.argv) == 2):
    cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # Capture frame-by-frame
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Display the resulting frame
    cv2.imshow('Video', image)
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
cv2.destroyAllWindows()

