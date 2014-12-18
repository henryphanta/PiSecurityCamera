#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime 
import subprocess
import twitterPost 


def securityStart():
    sensorPin = 7

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    prev = False
    curr = False

    cam = picamera.PiCamera()
    cam.vflip = True
    num = 1
    while True:
        prev = curr
        curr = GPIO.input(sensorPin)
        if curr != prev:
	    
            if curr:
                print "Camera on"
		picName = "img.jpeg"
                videoName = "video.h264"  
		cam.capture(picName)
                cam.start_recording(videoName)
           
                
            else:
                cam.stop_recording()
                print "Camera off"
		subprocess.call(["mv", "video.mp4", "securityCameraVideo/video" + str(num) + ".mp4"])
		num = num + 1
                subprocess.call(["MP4Box", "-add", videoName, "video.mp4"])  
                twitterPost.tweet()

securityStart()


