from djitellopy import Tello
from utils import CvFpsCalc

import cv2, math, time
import mediapipe as mp



def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Argument parsing
    in_flight = False

    # For webcam input:
    hands = mp_hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.5)

    # Camera preparation
    tello = Tello()
    tello.connect()
    tello.streamon()

    frame_read = tello.get_frame_read()

    # FPS Measurement
    cv_fps_calc = CvFpsCalc(buffer_len=5)

    while True:
        fps = cv_fps_calc.get()
        battery_status = tello.get_battery()

        # In reality you want to display frames in a seperate thread. Otherwise
        #  they will freeze while the drone moves.
        image = frame_read.frame

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Process Key (ESC: end)
        key = cv2.waitKey(1) & 0xff
        if key == 27: # ESCArgument parsing
            tello.land()
            break
        elif key == 32:
            if not in_flight:
                # Take-off drone
                tello.takeoff()
                in_flight = True
            elif in_flight:
                # Land tello
                tello.land()
                in_flight = False
        elif key == ord('w'):
            tello.move_forward(30)
        elif key == ord('s'):
            tello.move_back(30)
        elif key == ord('a'):
            tello.move_left(30)
        elif key == ord('d'):
            tello.move_right(30)
        elif key == ord('e'):
            tello.rotate_clockwise(30)
        elif key == ord('q'):
            tello.rotate_counter_clockwise(30)
        elif key == ord('r'):
            tello.move_up(30)
        elif key == ord('f'):
            tello.move_down(30)

        # Battery status and image rendering
        cv2.putText(image, "Battery: {} / fps:{}".format(battery_status, fps), (5, 720 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('DK_Drone', image)

    tello.land()
    tello.end()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
