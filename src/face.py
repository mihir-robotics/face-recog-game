# Face recognition code
# NEEDS TO BE REFACTORED
# Need to find way to optimize facial detection to reduce lag (multithread maybe?)

import imutils
from imutils.video import VideoStream
import numpy as np
import time 
import cv2

# File paths for Model and Weights
MODEL_PATH = ".\\model\\deploy.prototxt.txt"
ARCHITECTURE_PATH = ".\\model\\weights.caffemodel"

state = True

# Load the model, weight files, throw error if file path cannot be reolved
while state:
    try:
        # Load network from files
        net = cv2.dnn.readNetFromCaffe(MODEL_PATH, ARCHITECTURE_PATH)
        state = False
    except Exception:
        print('Error: Files not found')

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
# Delay
time.sleep(2)

# get face feed
def getFaceDetections(window_size):
    
    frame = vs.read()
    frame = imutils.resize(frame, width= window_size, height = window_size)

    height, width = frame.shape[:2]

    # Convert frame to a blob
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))
    net.setInput(blob)

    face_detections = net.forward()

    # Temporary returns, will change after drawFace()
    return face_detections, height, width, frame

# Draw Face on video stream, get X,y etc
def drawFace(face_detections, height, width, frame):
    startX, startY, endX, endY = 0 , 0, 0, 0
    for i in range(face_detections.shape[2]):
        confidence = face_detections[0, 0, i, 2]

        if confidence < 0.7:
            continue

        box =  face_detections[0,0,i,3:7] * np.array([width, height, width, height])
        (startX, startY, endX, endY) = box.astype('int')

        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        
    cv2.imshow('', frame)
    return startX, startY, endX, endY


# Clean-up routine to close all windows
def cleanup():
    cv2.destroyAllWindows()
    vs.stop