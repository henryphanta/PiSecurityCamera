#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime 
import subprocess
import twitterPost 

def getFileName():  
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

def securityStart():
    sensorPin = 7

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    prevState = False
    currState = False

    cam = picamera.PiCamera()

    while True:
        time.sleep(0.1)
        prevState = currState
        currState = GPIO.input(sensorPin)
        if currState != prevState:
            newState = "HIGH" if currState else "LOW"
            print "GPIO pin %s is %s" % (sensorPin, newState)
            if currState:
                #fileName = getFileName()
                videoName = "video.h264"  
                #cam.start_preview()
                cam.start_recording(videoName)
               # cam.capture(fileName)
                
            else:
                #cam.stop_preview()
                cam.stop_recording()
                subprocess.call(["rm", "video.mp4"])
                subprocess.call(["MP4Box", "-add", videoName, "video.mp4"])  
                twitterPost.tweet()

securityStart()


