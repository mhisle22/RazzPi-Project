from graphics import *
import picamera
import time

camera = picamera.PiCamera()
##win = GraphWin("Window", 600, 600)
##time.sleep(5)
      
camera.capture('/var/www/html/image.gif')
##picture = Image(Point(300,300), "image.gif")
####picture.draw(win)
####
####time.sleep(5)
##win.close()

