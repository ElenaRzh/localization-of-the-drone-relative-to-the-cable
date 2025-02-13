from ultralytics import YOLO
import cv2
import math

#Settings

IMAGE_HEIGHT = 1920
IMAGE_WIDTH = 1080

FIELD_OF_VIEW = 52
CAMERA_ANGLE = 52
DISTANCE_BETWEEN_CAMERAS = 0.98

#End settings

model = YOLO('cable.pt')

#cap_left = cv2.VideoCapture(1)
#cap_right = cv2.VideoCapture(2)

#cap_left.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap_left.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#cap_right.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap_right.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    #flag_l, img_l = cap_left.read()
    #flag_r, img_r = cap_right.read()

    img_r = cv2.imread('camera_r.jpg')
    img_l = cv2.imread('camera_l.jpg')

    results_r = model(source=img_r, show=True)
    results_l = model(source=img_l, show=True)

    coord_r = [0, 0, 0, 0]
    coord_l = [0, 0, 0, 0]

    for box in results_r[0].boxes.xyxy:
        for v in range(4):
            coord_r[v] = int(box[v])
    for box in results_l[0].boxes.xyxy:
        for v in range(4):
            coord_l[v] = int(box[v])

    cv2.circle(img_r, ((coord_r[2] - coord_r[0]) // 2 + coord_r[0], IMAGE_WIDTH // 2), 10, (255, 0, 0), -1)
    cv2.circle(img_l, ((coord_l[2] - coord_l[0]) // 2 + coord_l[0], IMAGE_WIDTH // 2), 10, (255, 0, 0), -1)

    cv2.imshow('R', cv2.resize(img_r, (1280, 720)))
    cv2.imshow('L', cv2.resize(img_l, (1280, 720)))

    angle_l = ((coord_l[2] - coord_l[0]) // 2 + coord_l[0]) * (FIELD_OF_VIEW / IMAGE_HEIGHT) + CAMERA_ANGLE
    angle_r = ((coord_r[2] - coord_r[0]) // 2 + coord_r[0]) * (FIELD_OF_VIEW / IMAGE_HEIGHT) + CAMERA_ANGLE

    pos_x = DISTANCE_BETWEEN_CAMERAS * math.tan(angle_r * math.pi / 180) / (math.tan(angle_l * math.pi / 180) + math.tan(angle_r * math.pi / 180))
    pos_y = math.tan(angle_l * math.pi / 180) * pos_x

    pos_x = round(pos_x - DISTANCE_BETWEEN_CAMERAS / 2, 3)
    pos_y = round(pos_y, 3)
    print(pos_x, pos_y)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
