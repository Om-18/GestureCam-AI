import cv2
import mediapipe as mp
import time
from picamera2 import Picamera2

# Camera setup
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

tip_ids = [4,8,12,16,20]

p_time = 0
monitoring = False

while True:

    frame = picam2.capture_array()
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    fingers = []

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):

                h, w, c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                lm_list.append((cx,cy))

            if lm_list:

                # Thumb
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0]-1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Other fingers
                for id in range(1,5):

                    if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id]-2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total = fingers.count(1)

                gesture_names = {
                    0: "FIST",
                    1: "ONE",
                    2: "TWO",
                    3: "THREE",
                    4: "FOUR",
                    5: "FIVE"
                }

                gesture = gesture_names.get(total,"")

                # ACTIONS
                if gesture == "ONE":
                    monitoring = True

                if gesture == "FIST":
                    monitoring = False

                if gesture == "TWO":
                    filename = f"capture_{int(time.time())}.jpg"
                    cv2.imwrite(filename, frame)
                    print("Photo saved:", filename)

                if gesture == "FIVE":
                    print("Exiting GestureCam AI")
                    break

                # UI BOX
                cv2.rectangle(frame,(10,10),(320,140),(0,0,0),-1)

                cv2.putText(frame,
                            f"Gesture: {gesture}",
                            (20,60),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0,255,0),
                            2)

                cv2.putText(frame,
                            f"Monitoring: {monitoring}",
                            (20,110),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (255,255,255),
                            2)

    # FPS Counter
    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time

    cv2.putText(frame,
                f"FPS: {int(fps)}",
                (500,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2)

    cv2.imshow("GestureCam AI", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
