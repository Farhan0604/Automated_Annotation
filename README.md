# YOLO11 Auto Annotation Tool (GUI Version)

A simple offline **GUI tool** that automatically annotates entire folders of images using the latest **YOLO11** object detection model.

Just select a folder → click **Run Annotation** → and the tool will:

- Annotate every image (bounding boxes + class labels)
- Generate a JSON file for each image (class, confidence, bounding box coordinates)
- Save everything inside the `output/` folder

No API keys, no cloud, no internet — everything runs locally.

---

## Features

-  **GUI interface** — no terminal needed  
- Select any folder of images  
- Automatically scans all images (JPG, PNG, JPEG, WEBP, BMP)  
- Fast object detection powered by YOLO11m  
- Saves:
  - Annotated image → `<image>_annotated.jpg`
  - JSON predictions → `<image>.json`
- Clean & modular code  
- No dependencies on external APIs  
- Works offline  

---

## Project Structure



auto_annotation/
│
├── src/
│ ├── annotate_yolo.py # YOLO annotator (handles detection + saving)
│ ├── gui.py # GUI application (Tkinter)
│ ├── utils.py # Optional helper utilities
│
├── main.py # (Unused if using GUI only)
├── output/ # Annotated results saved here
├── examples/ # Example images
├── requirements.txt
└── README.md


---

## 🔧 Installation
pip install -r requirements.txt

### 1. Clone the repository
```bash
git clone https://github.com/Farhan0604/<your-repo-name>.git
cd Automated_Annotation

```

## Run using 
python src/gui.py
