# Face recognition code
# NEEDS TO BE REFACTORED

from imutils.video import VideoStream
import imutils
import numpy as np
import argparse , time , cv2

#Constructing the argparse (I looked this part up online)
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")

args = vars(ap.parse_args())

# Loading the model (which I took from the internet)
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
time.sleep(2)

