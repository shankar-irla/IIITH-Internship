from ultralytics import YOLO as Y

# Load models
m = Y('yolov8n.pt')
m1 = Y('yolov8n-seg.pt')
m2 = Y('yolov8s.pt')
m3 = Y('yolov8m.pt')
m4 = Y('yolov8x.pt')
m5 = Y('yolov8l.pt')

# Predict and save results to custom folders
m1.predict(source="https://ultralytics.com/images/bus.jpg", save=True, name="nano-seg")
m.predict(source="bus.jpg", save=True, name="nano")
m2.predict(source="bus.jpg", save=True, name="small")
m3.predict(source="bus.jpg", save=True, name="medium")
m4.predict(source="bus.jpg", save=True, name="xlarge")
m5.predict(source="bus.jpg", save=True, name="large")
#predicting the test image
m1.predict(source="testimg.jpg", save=True, name="nano-seg_test")
m.predict(source="testimg.jpg", save=True, name="nano_test")
m2.predict(source="testimg.jpg", save=True, name="small_test")
m3.predict(source="testimg.jpg", save=True, name="medium_test")
m4.predict(source="testimg.jpg", save=True, name="xlarge_test")
m5.predict(source="testimg.jpg", save=True, name="large_test")