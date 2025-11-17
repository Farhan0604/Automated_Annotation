from ultralytics import YOLO

print("Downloading YOLO11 Base Model...")
model = YOLO("yolo11m.pt")
print("Done!")
