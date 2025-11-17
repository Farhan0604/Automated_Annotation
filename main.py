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
