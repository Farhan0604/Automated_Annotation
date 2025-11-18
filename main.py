"""
A simple command-line tool that uses YOLO11 for offline automatic image annotation.
It loads a YOLO model, detects objects in an image, and saves both the annotated
image and prediction results in JSON format.

"""

from src.annotate_yolo import YOLOAnnotator
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return

    image_path = sys.argv[1]

    annotator = YOLOAnnotator()
    annotator.annotate(image_path)

if __name__ == "__main__":
    main()
