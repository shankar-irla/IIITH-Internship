# Task-1: YOLOv8 Object Detection Setup

## 1. Created the Project Folder
- I created a new folder named **`YOLOv8_ObjectDetection_Internship`** to organize all project files in one place.

## 2. Set Up the Virtual Environment
- Opened the terminal in **VS Code** within the project folder and created a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activated the virtual environment:
  ```bash
  venv\Scripts\activate
  ```

## 3. Installed YOLOv8 Library
- After activating the virtual environment, I installed the YOLOv8 library:
  ```bash
  pip install ultralytics
  ```

## 4. Checked for GPU Support
- Verified if my system supports GPU using PyTorch:
  ```python
  import torch
  print(torch.cuda.is_available())
  ```
- It returned **True**, confirming that my system can run the YOLOv8 model faster using GPU.

## 5. Cloned the YOLOv8 Repository
- To explore the YOLOv8 source code in-depth, I cloned the official repository:
  ```bash
  git clone https://github.com/ultralytics/ultralytics.git
  cd ultralytics
  pip install -e .
  ```

## 6. Ran Object Detection
- I saved a test image named **`bus.jpg`** inside the project directory.
- Ran the YOLOv8 **nano model** (`yolov8n.pt`) for object detection:
  ```bash
  yolo detect predict model=yolov8n.pt source=bus.jpg
  ```
- The results were saved in:
  ```
  YOLOv8_ObjectDetection_Internship/results/detect/output/
  ```

## 7. Checked the Output
- Opened the **output folder** and found the processed image with detected objects, including labels and bounding boxes.  
- The model performed perfectly!
