# Task-5: Helmet Detection Project Using YOLOv8

## 1. Research Paper Selection
- Implementation was based on the IEEE paper:  
  **"Helmet Detection for Public Safety Monitoring using Deep Learning and YOLOv8."**

---

## 2. Dataset Acquisition
- Downloaded a **publicly available helmet detection dataset** from Kaggle.

---

## 3. Dataset Annotation
- Uploaded images to **Roboflow** for manual annotation.
- Annotated images with **bounding boxes** for helmet and non-helmet classes.

---

## 4. Exporting Dataset in YOLOv8 Format
- Downloaded the annotated dataset from Roboflow in **YOLOv8 format**, including:  
  - `train/` folder  
  - `valid/` folder  
  - `test/` folder  
  - Label `.txt` files for annotations

---

## 5. Virtual Environment Setup
- Created and activated a Python virtual environment named `helmetenv`.
- Installed necessary libraries:  
  - `ultralytics`  
  - `numpy`  
  - `opencv-python`

---

## 6. YOLOv8 Model Training
- Used Ultralytics YOLOv8 CLI command to train the model:
  ```
  yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=30 imgsz=640
  ```

---

## 7. Training Monitoring
- YOLOv8 automatically generated live metrics and graphs during training:
  - Loss  
  - Precision  
  - Recall  
  - mAP (mean Average Precision)

---

## 8. Model Evaluation
- After training, model performance on validation set was:  
  - **Precision:** 0.795  
  - **Recall:** 0.837  
  - **mAP@0.5:** 0.837  
  - **mAP@0.5:0.95:** 0.479

---

## 9. Testing Predictions
- Ran predictions on test images using:
  ```
  yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=your_test_folder/
  ```
- Prediction images with bounding boxes were saved in `runs/detect/predict/`.

---

## 10. Result Compilation
- Saved all relevant results including:  
  - Training graphs  
  - Confusion matrix  
  - Output prediction images

---

## Conclusion
This project demonstrated the effective use of YOLOv8 for helmet detection in public safety applications, achieving good precision and recall metrics.
