# Face recognition code
# NEEDS TO BE REFACTORED

from imutils.video import VideoStream
import imutils
import numpy as np
import argparse , time , cv2

#Constructing the argparse (I looked this part up online)
'''
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--prototxt", required=False, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=False, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.7, help="minimum probability to filter weak detections")

args = vars(ap.parse_args())
'''
# Loading the model (which I took from the internet)
net = cv2.dnn.readNetFromCaffe('model/deploy.prototxt.txt', 'model/res10_300x300_ssd_iter_140000.caffemodel')

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
time.sleep(2)

