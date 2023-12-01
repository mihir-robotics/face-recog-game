# Face recognition code
# NEEDS TO BE REFACTORED
# Need to find way to optimize facial detection to reduce lag (multithread maybe?)

# import setup to get absolute names for MODEL FILES
import setup
from imutils.video import VideoStream
import imutils
import numpy as np
import argparse , time , cv2

state = True

MODEL_PATH = setup.find_absolute_paths()[0]
ARCHITECTURE_PATH = setup.find_absolute_paths()[1]

# Loading the model (which I took from the internet)
# try until model is loaded
while state:
    try:
        net = cv2.dnn.readNetFromCaffe(MODEL_PATH, ARCHITECTURE_PATH)
        state = False
        print('loaded model')
    except Exception:
        print('cannot find file')
        pass

#net = cv2.dnn.readNetFromCaffe(MODEL_PATH, ARCHITECTURE_PATH)

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
time.sleep(2)

def cleanup():
    cv2.destroyAllWindows()
    vs.stop