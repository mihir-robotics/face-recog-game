''' 
Script handles the Face recognition libraries and functions
#. Modules:
-   Imutils
-   Numpy
-   OpenCV (cv2)
-   Time

#. Objects:
-   vs  (Video Stream Object)

#. Functions:
-   getFaceDetections():    Get frame and face detection from blob
-   drawFace():             Draw rectangle in cv2 window
-   cleanup():              Destroy cv2 window upon key-press
'''

# Import req. modules:
# OpenCV module
import cv2

# Basic image processing functions
import imutils
from imutils.video import VideoStream

# Numpy
import numpy as np

# For setting delay
import time 

# File paths for Model and Weights
MODEL_PATH = ".\\model\\deploy.prototxt.txt"
ARCHITECTURE_PATH = ".\\model\\weights.caffemodel"

# Load the model, weight files
net = cv2.dnn.readNetFromCaffe(MODEL_PATH, ARCHITECTURE_PATH)

#Initialise the Video Stream object 
vs = VideoStream(src=0).start()

# Set Time Delay
time.sleep(2)

# get face
def getFaceDetections(window_size):
    '''
    Obtain face detections from video stream, init. frame and network blob

    Input:
    -   window_size:    The dimensions of the cv2 window

    Returns:
    -   face_detections:    Detected face dimensions
    -   height:             Height of face frame
    -   width:              Width of face frame
    -   frame:              Frame object from video stream
    '''
    # Get the video frame
    frame = vs.read()
    # Resize
    frame = imutils.resize(frame, width= window_size, height = window_size)

    height, width = frame.shape[:2]

    # Convert frame to a blob
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))
    net.setInput(blob)
    # Get detections
    face_detections = net.forward()

    return face_detections, height, width, frame

# Draw Face on video stream, get X,y etc
def drawFace(face_detections, height, width, frame):
    '''
    Draw the detected face rectangle on cv2 window

    Inputs:
    -   face_detections:    Detected face dimensions
    -   height:             Height of face frame
    -   width:              Width of face frame
    -   frame:              Frame object from video stream

    Returns:
    -   startX, startY, endX, endY:    Co-ords of face rectangle, for use in sprite control/collision check...
    '''
    # Init. the co-ords
    startX, startY, endX, endY = 0, 0, 0, 0
    
    # Confidence threshold of detected face
    confidence_threshold = 0.7

    # Draw the rect.
    for i in range(face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]
        
        # Don't draw if confidence is less than threshold
        if confidence < confidence_threshold:
            continue

        box =  face_detections[0,0,i,3:7] * np.array([width, height, width, height])
        (startX, startY, endX, endY) = box.astype('int')

        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

    # Display the cv2 window  
    cv2.imshow('', frame)
    return startX, startY, endX, endY


# Clean-up routine to close all windows
def cleanup():
    '''
    Close out the windows, stop the video stream
    '''
    cv2.destroyAllWindows()
    vs.stop