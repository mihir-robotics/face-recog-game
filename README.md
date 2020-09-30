# Face Game OpenCV 

This program uses the DNN support provided by the cv2 module in python to track our face.
The co - ordinates of the face are then sent to the game, and the player character moves accordingly.

Inside the deploy.prototext.txt file is architecture of model, inside res10_300x300_ssd_iter_140000.caffemodel file are the weights for actual architecture model(layers).

Required Modules:
OpenCV for Python
NumPy 
Pygame
Argparse

Heres the command to run the code:

python faceGame2.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

Here's a YouTube video to demonstrate how the code works.

https://youtu.be/PgYPcLfHAvU
