import RPi.GPIO as GPIO
import time

import InstagramPostAutomated
import config
import webcam_capture

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def listenForGreedy():
    while True:
        if GPIO.input(18):
            print("Fatboy opened the fridge!!")
            webcam_capture.run_webcam_capture(1)
            instaBot = InstagramPostAutomated.InstagramPostAutomated(config.username, config.password)
            instaBot.login()
            instaBot.postImage()
        else:
            print("Door closed!")

        time.sleep(0.5)