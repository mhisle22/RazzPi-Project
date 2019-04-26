import picamera, time

camera = picamera.PiCamera()
camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
camera.close()
