from picamera2 import Picamera2
import time

picam = Picamera2()

picam.start()

time.sleep(2)   # allow camera to adjust exposure

picam.capture_file("image.jpg")

print("Image captured!")
