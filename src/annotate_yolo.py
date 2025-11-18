from ultralytics import YOLO
import cv2

class YOLOAnnotator:
    """
    A lightweight YOLO11-based annotator for detecting objects in images.
    Automatically saves an annotated image and a JSON file with predictions.
    """
    def __init__(self, model_name="yolo11m.pt"):
        print("[*] Loading YOLO11 model...")
        self.model = YOLO(model_name)

    def annotate(self, image_path, output_image_path="output/annotated_yolo.jpg"):
        print("[*] Running detection...")

        # Run YOLO prediction
        results = self.model(image_path)[0]

        # YOLO returns an annotated image array
        annotated = results.plot()

        # Save the annotated image
        cv2.imwrite(output_image_path, annotated)
        print(f"[✓] Annotated image saved to {output_image_path}")

        # Print detections
        print("\nDetected objects:")
        for box in results.boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            name = self.model.names[cls]
            print(f" - {name} ({conf:.2f})")

        return results
