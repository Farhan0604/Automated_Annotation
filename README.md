# YOLO Auto Image Annotation Tool

A simple offline tool that automatically annotates images using the YOLO11 model.

## Features
- Offline object detection
- Annotates images using YOLO11
- Saves predictions as JSON
- Saves annotated images
- Supports any image type

## Installation
pip install -r requirements.txt

## Usage

### Annotate a single image:
python main.py examples/loaf_cat.jpeg

### Output:
- `output/annotated_yolo.jpg`
- `output/predictions.json`

## Project Structure

auto_annotation/
src/
examples/
output/
main.py
requirements.txt
README.md


## Model
The project uses the YOLO11m model (downloaded automatically).

