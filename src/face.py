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


# Clean-up routine to close all windows
def cleanup():
    cv2.destroyAllWindows()
    vs.stop