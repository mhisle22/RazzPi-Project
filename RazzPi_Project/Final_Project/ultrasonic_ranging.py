#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

TRIG = 32
ECHO = 18

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
        while True:
                time.sleep(4)
                dis = distance()
                print '{0:.4g}'.format(dis), 'cm'
                filename = open("output.txt","w")
                filename.write(str('{0:.4g}'.format(dis)))
                filename.close()
                sys.exit()

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
