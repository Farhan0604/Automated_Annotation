# gui.py
import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from src.annotate_yolo import YOLOAnnotator

VALID_IMAGES = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

class AnnotatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YOLO11 Auto Annotation Tool")
        self.root.geometry("600x350")

        self.folder_path = tk.StringVar()

        tk.Label(self.root, text="YOLO11 Auto-Annotation", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Choose a folder containing images").pack()

        tk.Button(self.root, text="Browse Folder", command=self.browse_folder, width=20).pack(pady=5)

        tk.Entry(self.root, textvariable=self.folder_path, width=60).pack(pady=5)

        tk.Button(self.root, text="Run Annotation", command=self.start_annotation, width=20).pack(pady=10)

        self.output_box = tk.Text(self.root, height=10, width=70)
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
        self.log("Loading YOLO model...")
        annotator = YOLOAnnotator()

        images = [f for f in os.listdir(folder) if f.lower().endswith(VALID_IMAGES)]
        if not images:
            self.log("No valid images found in folder.")
            return

        os.makedirs("output", exist_ok=True)

        total = len(images)
        self.log(f"Found {total} images.")

        for i, img_name in enumerate(images, start=1):
            img_path = os.path.join(folder, img_name)

            out_img = f"output/{img_name}_annotated.jpg"
            out_json = f"output/{img_name}.json"

            count = annotator.annotate_image(img_path, out_img, out_json)

            self.log(f"[{i}/{total}] {img_name} → {count} objects")

        self.log("\n✔ DONE — All images processed.")

    def log(self, text):
        self.output_box.insert(tk.END, text + "\n")
        self.output_box.see(tk.END)


if __name__ == "__main__":
    AnnotatorGUI()
