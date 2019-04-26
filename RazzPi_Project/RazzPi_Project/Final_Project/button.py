#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys

BtnPin = 38
Gpin   = 33
Rpin   = 37
var = 0

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(40, GPIO.OUT)
	GPIO.setup(29, GPIO.OUT)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

def Print(x):
        if x == 0:
                print("Pressed!")
                GPIO.output(40, 1)
                GPIO.output(29, 1)
        elif x == 1:
                GPIO.output(40, 0)
                GPIO.output(29, 0)
                print("Not pressed!")

def detect(chn):
	#Led(GPIO.input(BtnPin))
        global var
        var += 1
        Print(GPIO.input(BtnPin))

def loop():
        while True:
                if var >= 6:
                        GPIO.cleanup()
                        sys.exit()
	

def destroy():
        GPIO.output(40, 0)
        GPIO.output(29, 0)
        GPIO.output(31, 0)
        GPIO.output(22, 0)
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

