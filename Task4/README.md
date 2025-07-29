# Task-4: Custom Object Detection Model with YOLOv8

## 1. Project Initialization
- Began building a **custom object detection model** using **YOLOv8** with a **self-collected dataset**.

---

## 2. Data Collection
- **Gathered a set of images** containing the objects to be detected by the model.

---

## 3. Image Labeling
- Used an annotation tool to **draw bounding boxes** around the objects in each image.
- Saved the labels in the **YOLO-compatible format**.

---

## 4. Dataset Organization
- **Separated the dataset** into:
  - **Training set** (for model learning).
  - **Testing set** (for evaluating performance).
- Created structured folders for images and labels.

---

## 5. Configuration Setup
- Created a **YAML configuration file** specifying:
  - Dataset paths (train/test).
  - Number of classes.
  - Class names.

---

## 6. Model Training
- Trained the **YOLOv8 model** on the custom dataset.
- The training completed successfully **without any errors**.

---

## 7. Model Testing
- Evaluated the trained model on **test images** to check detection accuracy.

---

## 8. Observations
- **Low accuracy on new images**, indicating that the model failed to generalize properly.

---

## 9. Root Cause
- Identified that the dataset was:
  - **Too small** or
  - **Not diverse enough**,  
  leading to **overfitting**.

---

## 10. Key Learnings
- Gained hands-on experience in building a **YOLOv8 object detection pipeline** from scratch.
- Understood the **critical role of high-quality and diverse datasets** in achieving good model performance.
