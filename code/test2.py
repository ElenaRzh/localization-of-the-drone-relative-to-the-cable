import time
import numpy as np
import cv2
import math

#Settings

IMAGE_HEIGHT = 1920
IMAGE_WIDTH = 1080

FIELD_OF_VIEW = 52
CAMERA_ANGLE = 70
DISTANCE_BETWEEN_CAMERAS = 0.98

#End settings

detected_cable_r = []
detected_cable_l = []
detected_cable_pos = []

def cable_detect(cable_mask, frame):
    for g in range(IMAGE_WIDTH // 10):
        for i in range(IMAGE_HEIGHT):
            count = 0
            for m in range(10):
                if cable_mask[i][g*10 + m] == 255:
                    count += 1
            if count > 7:
                cable_mask[i][g*10] = 255
                cv2.circle(frame, (g*10, i), 2, (255, 0, 0), -1)
            else:
                cable_mask[i][g*10] = 0

        for i in range(2, IMAGE_HEIGHT-3):
            if cable_mask[i][g*10] == 255 and cable_mask[i-1][g*10] == 0 and cable_mask[i-2][g*10] == 255:
                cable_mask[i - 1][g*10] = 255

        start_x = -1
        cable = []
        n = 0

        for i in range(IMAGE_HEIGHT):
            if cable_mask[i][g*10] == 255 and start_x == -1:
                start_x = i
            if cable_mask[i][g*10] == 0 and start_x != -1:
                #if  i - start_x > 4:
                    #cable.append((int((i - start_x) / 2 + start_x), i - start_x))
                start_x = -1
                n += 1

        for i in range(len(cable)):
            cv2.circle(frame, (g*10, cable[i][0]), 6, (0, 255, 0), -1)

    return frame

#cap_left = cv2.VideoCapture(1)
#cap_right = cv2.VideoCapture(2)

#cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    mask_l = np.zeros((1920, 1080), dtype = "uint8")
    mask_r = np.zeros((1920, 1080), dtype = "uint8")
    for i in range(3):
        #flag_l, frame_l = cap_left.read()
        #flag_r, frame_r = cap_right.read()

        frame_l = cv2.imread('camera_l-1.jpg')
        frame_r = cv2.imread('camera_r-1.jpg')

        frame_l = cv2.rotate(frame_l, cv2.ROTATE_90_COUNTERCLOCKWISE)
        frame_r = cv2.rotate(frame_r, cv2.ROTATE_90_CLOCKWISE)

        #frame_l = cv2.fastNlMeansDenoisingColored(frame_l, None, 10, 10, 7, 21)
        #frame_r = cv2.fastNlMeansDenoisingColored(frame_r, None, 10, 10, 7, 21)

        hsv_img_r = cv2.cvtColor(frame_r, cv2.COLOR_BGR2HSV)
        hsv_img_l = cv2.cvtColor(frame_l, cv2.COLOR_BGR2HSV)

        mask_r = cv2.bitwise_or(cv2.inRange(hsv_img_r, (0, 0, 70), (180, 39, 174)), mask_r)
        mask_l = cv2.bitwise_or(cv2.inRange(hsv_img_l, (0, 0, 70), (180, 39, 174)), mask_l)

        #mask_l = cv2.fastNlMeansDenoising(mask_l, None, 10, 7, 21)
        #mask_r = cv2.fastNlMeansDenoising(mask_r, None, 10, 7, 21)

    cv2.imshow('G2', cv2.resize(mask_r, (720, 1280)))
    cv2.imshow('H2', cv2.resize(mask_l, (720, 1280)))

    cv2.imshow('G', cv2.resize(cable_detect(mask_r, frame_r), (720, 1280)))
    cv2.imshow('H', cv2.resize(cable_detect(mask_l, frame_l), (720, 1280)))

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
