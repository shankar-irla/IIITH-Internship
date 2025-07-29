from ultralytics import YOLO

def trainmodel():
    # Load a model
    model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
    # Train the model
    results = model.train(data="african-wildlife.yaml", epochs=20, imgsz=640)

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  # Optional but safe
    trainmodel()