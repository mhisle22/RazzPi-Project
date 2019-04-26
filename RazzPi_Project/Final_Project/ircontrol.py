#!/usr/bin/python

import pylirc, time
import RPi.GPIO as GPIO
import os
import sys
from graphics import *
import threading

IrPin  = 16
blocking = 0
power = True
option = 1

def setup():
        
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setwarnings(False)
        os.system("python2 lcd1602.py 0")
        pylirc.init("pylirc", "./conf", blocking)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def option(config):

        global power
        done = False
        #each if represents a button on remote and a sensor to go along with it
        #greeting
        if config == 'KEY_NUMERIC_1' and power == True:
                print 'Option 1'
                message(1)
                os.system("python2 lcd1602.py 1")
                done = True
                time.sleep(1)
        #touch sensor
        if config == 'KEY_NUMERIC_2' and power == True:
                print 'Option 2'
                message(2)
                print 'Handshake!'
                os.system("python2 touch_switch.py")
                os.system("python2 lcd1602.py 2")
                done = True
                time.sleep(1)
        #button & lights
        if config == 'KEY_NUMERIC_3' and power == True:
                print 'Option 3'
                message(3)
                print 'Button!'
                os.system("python2 button.py")
                os.system("python2 lcd1602.py 3")
                print "Finished!"
                time.sleep(1)
        #tilt sensor
        if config == 'KEY_NUMERIC_4' and power == True:
                print 'Option 4'
                message(4)
                print 'Tilt!'
                os.system("python2 tilt_switch.py")
                os.system("python2 lcd1602.py 4")
                print "Finished!"
                time.sleep(1)
        #range finder        
        if config == 'KEY_NUMERIC_5' and power == True:
                print 'Option 5'
                message(5)
                print 'Distance.'
                os.system("python2 ultrasonic_ranging.py")
                os.system("python2 lcd1602.py 5")
                print "Finished!"
                time.sleep(1)
        #passive buzzer
        if config == 'KEY_NUMERIC_6' and power == True:
                print 'Option 6'
                message(6)
                print 'Sound.'
                os.system("python2 passive_buzzer.py")
                os.system("python2 lcd1602.py 6")
                print "Finished!"
                time.sleep(1)

        #calculator code is in here instead. And looks terrible ¯\_(ツ)_/¯
        #                                                           |
        #                                                           |
        #                                                           /\
        if config == 'KEY_NUMERIC_7' and power == True:
                print 'Option 7'
                message(7)
                print 'Calculator.'
                array1 = []
                filename = open("output.txt","w")
                while True:
                        s = pylirc.nextcode(1)
                        while(s):
                                for (code) in s:
                                        
                                        array1 = calculator(code["config"], array1)
                                        if len(array1) != 0 and array1[-1] == "=":
                                                array1.pop()
                                                total = ""
                                                for element in array1:
                                                        total += element
                                                print total
                                                filename.write(total + "\n")
                                                if "+" in total:
                                                        array1 = total.split("+")
                                                        num = int(array1[0]) + int(array1[1])
                                                        print num
                                                        filename.write(str(num))
                                                        done = True
                                                        break
                                                else:
                                                        array1 = total.split("-")
                                                        num = int(array1[0]) - int(array1[1])
                                                        print num
                                                        filename.write(str(num))
                                                        done = True
                                                        break
                                                        
                                if(not blocking):
                                        s = pylirc.nextcode(1)
                                else:
                                        s = []
                        if done:
                                break
                filename.close()
                os.system("python2 lcd1602.py 7")
                time.sleep(1)
        #camera. Picture is displayed here.
        if config == 'KEY_NUMERIC_8' and power == True:
                print 'Option 8'
                message(8)
                os.system("sudo rm /var/www/html/image.gif") #get rid of old copy
                print 'Camera.'
                os.system("python2 lcd1602.py 8")
                os.system("python2 camera.py")
                time.sleep(1)
                print 'Finished!'
        #video
        if config == 'KEY_NUMERIC_9' and power == True:
                print 'Option 9'
                message(9)
                print 'Video.'
                os.system("python2 video_camera.py")
                os.system("python2 lcd1602.py 9")
                os.system("sudo omxplayer /usr/lib/cgi-bin/video.h264")
                time.sleep(1)
                print 'Finished!'
        #possible bonus feature?
        if config == 'KEY_CHANNEL' and power == True:
                print 'Russian mode.'
                os.system("python2 lcd1602.py 420")
        #power button stops it
        if config == 'KEY_CHANNELDOWN' and power == True:
                print 'Power Off!'
                message(10)
                os.system("python2 lcd1602.py 11")
                power = False
                time.sleep(3)
                os.system("python2 lcd1602.py 0")
        elif config == 'KEY_CHANNELDOWN' and power == False:
                power = True
                print 'Power On!'
                
        return done

def calculator(config, arrayOn):

        if config == 'KEY_NUMERIC_1':
                arrayOn.append("1")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_2':
                arrayOn.append("2")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_3':
                arrayOn.append("3")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_4':
                arrayOn.append("4")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_5':
                arrayOn.append("5")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_6':
                arrayOn.append("6")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_7':
                arrayOn.append("7")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_8':
                arrayOn.append("8")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_NUMERIC_9':
                arrayOn.append("9")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_VOLUMEDOWN':
                arrayOn.append("=")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_VOLUMEUP':
                arrayOn.append("-")
                print arrayOn[-1]
                time.sleep(1)
        if config == 'KEY_EQUAL':
                arrayOn.append("+")
                print arrayOn[-1]
                time.sleep(1)
                
        return arrayOn

#takes care of html bs
def message(option):
        filename = open("display.txt","w")
        if option == 1:
                filename.write("Nikolai says hello. ")
                filename.write("Do you see the display screen?")
        if option == 2:
                filename.write("Touch the circle on the touch switch ")
                filename.write("to shake Nikolai's... hand.")
        if option == 3:
                filename.write("Press and hold the button to turn on the lights. ")
                filename.write("Release it and they will turn off.")
        if option == 4:
                filename.write("Tilt the tilt switch to tilt Nikolai. ")
                filename.write("Hope Nikolai isn't afraid of falling!\nWatch the Dual-Color LED change colors as you tilt.")
        if option == 5:
                filename.write("Stand in front of the ultrasonic ranging device ")
                filename.write("to be found. Try putting your hand up next.")
        if option == 6:
                filename.write("Nikolai will play a song from the buzzer. ")
                filename.write("Upgrade to premium to unlock new songs!")
        if option == 7:
                filename.write("Use the remote to send in one number, ended by the plus ")
                filename.write("or minus button, then the next number follow by EQ.")
        if option == 8:
                filename.write("camera\n")
                filename.write("The camera is on the end of the white ribbon. ")
                filename.write("")
        if option == 9:
                filename.write("video\n")
                filename.write("Nikolai will record a 5 second video ")
                filename.write("from the camera.")
        if option == 10:
                filename.write("")
        filename.close()

def loop():
        done = False
        while True:
                s = pylirc.nextcode(1)
                while(s):
                        for(code) in s:
                                done = option(code["config"])
                        if done:
                                print "Finished!"
                                break
                        elif(not blocking):
                                s = pylirc.nextcode(1)
                        else:
                                s = []
                        
                
def destroy():
	
	GPIO.cleanup()
	pylirc.exit()

def browser():
        os.system("chromium-browser 10.14.2.243/start.html --no-sandbox")
                


if __name__ == '__main__':
        try:
                setup()
                t1 = threading.Thread(target=browser)
                t2 = threading.Thread(target=loop)
                t1.start()
                t2.start()
		#loop()
        except KeyboardInterrupt:
                destroy()

