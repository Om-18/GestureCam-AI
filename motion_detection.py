from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()
picam2.start()

time.sleep(2)

previous_frame = None

while True:
    
    frame = picam2.capture_array()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if previous_frame is None:
        previous_frame = gray
        continue

    frame_diff = cv2.absdiff(previous_frame, gray)
    thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]

    motion_score = thresh.sum()

    if motion_score > 500000:
        
        filename = f"motion_images/motion_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)

        print("Motion detected! Image saved:", filename)

        time.sleep(2)

    previous_frame = gray
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break
