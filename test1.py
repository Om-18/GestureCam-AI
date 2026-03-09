import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start()

prev_frame = None

while True:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is None:
        prev_frame = gray
        continue

    diff = cv2.absdiff(prev_frame, gray)
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

    motion = thresh.sum()

    if motion > 100000:
        print("Motion detected!")
        cv2.imwrite("motion.jpg", frame)

    prev_frame = gray
