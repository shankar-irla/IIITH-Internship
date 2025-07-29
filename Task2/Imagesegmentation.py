from ultralytics import YOLO
import os
import cv2

# Load YOLOv8 segmentation model
model = YOLO("yolov8x-seg.pt")

input_images = r"P:\IIITH Internship\Task2\InputIMG"
output_images = r"P:\IIITH Internship\Task2\OUTPUTIMG\Seg-Images"
os.makedirs(output_images, exist_ok=True)

for file in sorted(os.listdir(input_images)):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_images, file)
        results = model.predict(img_path)
        for result in results:
            annotated_img = result.plot()
            save_path = os.path.join(output_images, file)
            cv2.imwrite(save_path, annotated_img)

input_frames = r"P:\IIITH Internship\Task2\InputIMG\frames"
output_frames = r"P:\IIITH Internship\Task2\OUTPUTIMG\Seg-Frames"
os.makedirs(output_frames, exist_ok=True)

for file in sorted(os.listdir(input_frames)):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_frames, file)
        results = model.predict(img_path)
        for result in results:
            annotated_img = result.plot()
            save_path = os.path.join(output_frames, file)
            cv2.imwrite(save_path, annotated_img)