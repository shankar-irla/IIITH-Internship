# Task-3: YOLOv8 Object Detection on African-Wildlife Dataset

## 1. Dataset Setup
- The **African-Wildlife dataset** containing **4 animal classes** was downloaded and unzipped into the working directory.
- The dataset includes a balanced distribution of classes (400–575 images per class).

---

## 2. Model Used
- **YOLOv8n (nano version)** was selected for its **lightweight design** and **efficient real-time performance**.
- The model was trained on the African-Wildlife dataset to detect all four animal classes effectively.

---

## 3. Key Evaluation Metrics & Insights

### **Confusion Matrix**
- Strong diagonal indicating correct classifications for all classes.
- Most errors were due to animals being misclassified as **background** (missed detections), rather than confusion with other animal classes.

### **F1-Confidence Curve**
- **Best F1 Score:** `0.91` at **0.575 confidence**.
- **Class-wise Performance:**
  - **Rhino** performed best.
  - **Elephant** showed the lowest F1 score.
- At higher confidence thresholds, the model became **overly conservative**, reducing recall.

### **Precision-Confidence Curve**
- Achieved **1.0 precision** at **0.97 confidence**.
- Gradual increase in precision indicates a few incorrect predictions in mid-confidence ranges.

### **Precision-Recall Curve**
- High **mAP** ranging from **0.946 to 0.959** with rectangular curves.
- Indicates stable and consistent model performance across all classes.

### **Recall-Confidence Curve**
- Started with **98% recall**, dropping sharply after **0.8 confidence threshold**.
- Shows the model may **miss valid detections** when the confidence threshold is set too high.

---

## 4. Training & Data Balance
- Training and validation metrics showed **smooth convergence**, with no signs of overfitting.
- Balanced class distribution ensured fair detection performance across all animal categories.

---

## 5. Conclusion
The YOLOv8n model achieved **high accuracy** with a strong **mAP (0.95)** and **F1-score (0.91)**, making it highly effective for wildlife detection tasks.
