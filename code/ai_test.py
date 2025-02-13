from ultralytics import YOLO
import cv2

model = YOLO('cable.pt')

img_r = cv2.imread('camera_r.jpg')

results = model(source=img_r, show=True)

coord = [0,0,0,0]

for box in results[0].boxes.xyxy:
    for v in range(4):
        coord[v] = int(box[v])
print(coord)
