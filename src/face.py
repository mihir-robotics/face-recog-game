# Face recognition code
# NEEDS TO BE REFACTORED

from imutils.video import VideoStream
import imutils
import numpy as np
import argparse , time , cv2

# Loading the model (which I took from the internet)
net = cv2.dnn.readNetFromCaffe('model/deploy.prototxt.txt', 'model/res10_300x300_ssd_iter_140000.caffemodel')

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
time.sleep(2)

