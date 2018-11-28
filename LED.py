import RPi.GPIO as GPIO
import time

def timeblinking():
	for i in range (10):
		if i % 3 == 0:
			time.sleep(i)
			print "LED on"
			GPIO.output(18, GPIO.HIGH)
		else:
			time.sleep(i)
			print "LED off"
			GPIO.output(18, GPIO.LOW)

def blinks(nums):
	time.sleep(0.5)
	for i in range (nums):
		GPIO.output(18, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(18, GPIO.LOW)
		time.sleep(0.2)
		

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
blinks(3)



