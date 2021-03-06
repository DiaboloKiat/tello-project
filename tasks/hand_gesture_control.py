#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configargparse

import cv2 as cv

from gestures.tello_gesture_controller import TelloGestureController
from utils import CvFpsCalc

from djitellopy import Tello
from gestures import *

import threading

def main():
    # init global vars
    global gesture_buffer
    global gesture_id

    # Argument parsing
    KEYBOARD_CONTROL = True
    WRITE_CONTROL = False
    in_flight = False

    # Camera preparation
    tello = Tello()
    tello.connect()
    tello.streamon()

    cap = tello.get_frame_read()

    # Init Tello Controllers
    gesture_controller = TelloGestureController(tello)
    keyboard_controller = TelloKeyboardController(tello)

    gesture_detector = GestureRecognition(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    gesture_buffer = GestureBuffer(buffer_len=5)

    def tello_control(key, keyboard_controller, gesture_controller):
        global gesture_buffer

        if KEYBOARD_CONTROL:
            keyboard_controller.control(key)
        else:
            gesture_controller.gesture_control(gesture_buffer)

    # FPS Measurement
    cv_fps_calc = CvFpsCalc(buffer_len=10)

    mode = 0
    number = -1
    battery_status = -1

    while True:
        fps = cv_fps_calc.get()
        battery_status = tello.get_battery()

        # Process Key (ESC: end)
        key = cv.waitKey(1) & 0xff
        if key == 27:  # ESC
            break
        elif key == 32:  # Space
            if not in_flight:
                # Take-off drone
                tello.takeoff()
                in_flight = True
                tello.move_up(50)
            elif in_flight:
                # Land tello
                tello.land()
                in_flight = False

        elif key == ord('k'):
            mode = 0
            KEYBOARD_CONTROL = True
            WRITE_CONTROL = False
            tello.send_rc_control(0, 0, 0, 0)  # Stop moving
        elif key == ord('g'):
            KEYBOARD_CONTROL = False
        elif key == ord('n'):
            mode = 1
            WRITE_CONTROL = True
            KEYBOARD_CONTROL = True

        if WRITE_CONTROL:
            number = -1
            if 48 <= key <= 57:  # 0 ~ 9
                number = key - 48

        # Camera capture
        image = cap.frame

        debug_image, gesture_id = gesture_detector.recognize(image, number, mode)
        gesture_buffer.add_gesture(gesture_id)

        # Start control thread
        threading.Thread(target=tello_control, args=(key, keyboard_controller, gesture_controller,)).start()
        threading.Thread(target=battery_status, args=(tello,)).start()

        debug_image = gesture_detector.draw_info(debug_image, fps, mode, number)

        # Battery status and image rendering
        cv.putText(debug_image, "Battery: {}".format(battery_status), (5, 720 - 5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.imshow('Tello Gesture Recognition', debug_image)

    tello.land()
    tello.end()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()










