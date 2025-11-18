# src/annotate_yolo.py

from ultralytics import YOLO
import cv2
import json
import os

class YOLOAnnotator:
    """
    A lightweight YOLO11-based annotator for detecting objects in images.
    Automatically saves an annotated image and a JSON file with predictions.
    """

    def __init__(self, model_name="yolo11m.pt"):
        print("[*] Loading YOLO11 model...")
        self.model = YOLO(model_name)

    def annotate_image(self, image_path, output_img_path, output_json_path):
        """
        Runs YOLO detection on a single image and saves:
        - annotated image (with bounding boxes)
        - JSON predictions file
        """
        results = self.model(image_path)[0]

        # Save annotated image
        annotated = results.plot()
        cv2.imwrite(output_img_path, annotated)

        # Save JSON predictions
        boxes = []
        for box in results.boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            name = self.model.names[cls]
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            boxes.append({
                "class": name,
                "confidence": conf,
                "bbox": [x1, y1, x2, y2]
            })

        with open(output_json_path, "w") as f:
            json.dump({"predictions": boxes}, f, indent=4)

        return len(boxes)
