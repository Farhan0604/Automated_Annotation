"""
A simple Tkinter GUI tool for automatically annotating all images in a folder
using the YOLO11 object detection model. The tool scans the selected directory,
runs detection on each image, and saves both annotated images and JSON results
in the output folder.
"""

import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from src.annotate_yolo import YOLOAnnotator

VALID_IMAGES = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


YOLO_INSTANCE = YOLOAnnotator()


class AnnotatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YOLO11 Auto Annotation Tool")
        self.root.geometry("650x400")

        self.folder_path = tk.StringVar()

        tk.Label(self.root, text="YOLO11 Auto-Annotation Tool", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Choose a folder containing images").pack()

        tk.Button(self.root, text="Browse Folder", command=self.browse_folder, width=20).pack(pady=5)

        tk.Entry(self.root, textvariable=self.folder_path, width=70).pack(pady=5)

        tk.Button(self.root, text="Run Annotation", command=self.start_annotation, width=20).pack(pady=10)

        self.output_box = tk.Text(self.root, height=12, width=80)
        self.output_box.pack()

        self.root.mainloop()

    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.folder_path.set(folder)

    def start_annotation(self):
        folder = self.folder_path.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid folder.")
            return

        threading.Thread(target=self.run_annotation, args=(folder,), daemon=True).start()

    def run_annotation(self, folder):
        self.log("Using preloaded YOLO model...")

        annotator = YOLO_INSTANCE 

        # Scan all images
        images = []
        for root, _, files in os.walk(folder):
            for f in files:
                if f.lower().endswith(VALID_IMAGES):
                    images.append(os.path.join(root, f))

        if not images:
            self.log("No valid images found in folder.")
            return

        os.makedirs("output", exist_ok=True)

        total = len(images)
        self.log(f"Found {total} images to annotate...\n")

        # Loop through ALL images
        for i, img_path in enumerate(images, start=1):
            img_name = os.path.basename(img_path)

            out_img = f"output/{img_name}_annotated.jpg"
            out_json = f"output/{img_name}.json"

            count = annotator.annotate_image(img_path, out_img, out_json)

            self.log(f"[{i}/{total}] {img_name} → {count} objects detected")

        self.log("\n✔ DONE — All images processed successfully.")

    def log(self, text):
        self.output_box.insert(tk.END, text + "\n")
        self.output_box.see(tk.END)


if __name__ == "__main__":
    AnnotatorGUI()
