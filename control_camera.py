import RPi.GPIO as GPIO
import time
import cv2


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True: 
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        ret,frame = cap.read() # return a single frame in variable `frame`
        cv2.imwrite('1.png',frame)
        time.sleep(1)



cap.release()

