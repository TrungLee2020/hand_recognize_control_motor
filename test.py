from builtins import set

import tensorflow as tf
import os

import copy
import math
import requests
import operator
import time
import datetime


from PIL import Image
import numpy as np
import cv2
import serial

serial_ = serial.Serial('COM3', 9600)
print(serial_.readline())


# parameters
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8  # start point/total width
#threshold = 60  #  BINARY threshold
#blurValue = 9  # GaussianBlur parameter
bgSubThreshold = 50

i = 0

# Camera
camera = cv2.VideoCapture(0)
camera.set(10,200)
label = []
continuos=False

while i<1:
    while camera.isOpened():

        ret, frame = camera.read()
        k = cv2.waitKey(10)
        if k == 27:  # press ESC to exit
            cv2.destroyAllWindows()
            break

        elif k == ord('a'):
            print(label)
            if (label=="07_ok"):
                ok = '1'
                serial_.write(ok.encode())   #send 1 to arduino
                print("OK")
            elif(label=="02_l"):
                l = "2"
                serial_.write(l.encode())   # send 2 to arduino
                print("Stop")
