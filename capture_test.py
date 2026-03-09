from picamera2 import Picamera2
import time

picam = Picamera2()
picam.start()

while True:
    input("Press ENTER to capture image")

    filename = f"photo_{int(time.time())}.jpg"
    picam.capture_file(filename)

    print("Saved:", filename)
