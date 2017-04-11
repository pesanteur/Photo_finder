import face_recognition as fr
from cv2 import *

# Sample code for taking photo with webcam. This will be used to help find all photos
# on a computer with your face in it and organize those accordingly
# Get a reference to camera
# Code works on MacOS but not yet on Linux
cam = VideoCapture(0)
s, img = cam.read()
if s:
    namedWIndow("cam-test", CV_WINDOW_AUTOSIZE)
    imshow('cam-test', img)
    waitKey(0)
    destroyWindow('cam-test')
    imwrite('photoofme.jpg', img) #Save image
