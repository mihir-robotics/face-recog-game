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

# Clean-up routine to close all windows
def cleanup():
    cv2.destroyAllWindows()
    vs.stop