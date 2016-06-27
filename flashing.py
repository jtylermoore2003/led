import RPi.GPIO as GPIO
import time

Green = 4
Red = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Red, GPIO.OUT)


for i in range(1,6):
    GPIO.output(Green, True)
    time.sleep(1)
    GPIO.output(Green, False)
    time.sleep(1)
    GPIO.output(Red, True)
    time.sleep(1)
    GPIO.output(Red, False)
    time.sleep(1)
