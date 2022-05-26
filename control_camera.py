#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import cv2
import usb_trial
import os
from dronekit import connect
import datetime
import timeit
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
vehicle = connect('/dev/ttyACM0', wait_ready = True, baud = 115200)
e = datetime.datetime.now()
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3264)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)

reset_time = 0 

i = 1
folder = 1

try:
    root = str((usb_trial.get_mount_points()[0][1]))
    
    #root = '/home/pi/Desktop/fixedwing-mangrove'
    print(root)
    path = root + '/flight'+str(folder)+'/'
    while(os.path.isdir(path)):
        #fold_dir = 'folder'+str(folder)
        #print("%s exists",fold_dir)
        folder+=1
        #print('right before path')
        path = root +'/flight'+str(folder)
        #print('right after path')
    os.mkdir(path)
except:
    path = ""
    

print("Ready for image")

while True:
    ret,frame = cap.read() # return a single frame in variable `frame`
    #ims = cv2.resize(frame, (640, 480))
    #cv2.imshow('preview', ims)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    if (GPIO.input(10) == GPIO.HIGH) and (time.time() > (reset_time + 1)):
        print("Button was pushed!")
        lat = str(vehicle.location.global_relative_frame.lat)
        lon = str(vehicle.location.global_relative_frame.lon)
        alt = str(vehicle.location.global_relative_frame.alt)
        date = str(e.strftime("%Y-%m-%d %H:%M:%S"))
        print(path)
        cv2.imwrite(os.path.join(path, date+' '+lat+' '+lon+' '+alt+'.jpg'),frame)
#         i+=1

            
        
        



cap.release()

