import torch
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path

# STEP 1: Load the YOLOv5 model
print("Loading YOLOv5 model...")
model = torch.hub.load("yolov5", "custom", path="yolov5s.pt", source="local")

# Set paths
image_folder = Path("images")
# if not image_folder.exists():
#     print(f"Error: Directory {image_folder} does not exist!")
#     exit()

output_folder = Path("detection_results")
output_folder.mkdir(exist_ok=True)  # Ensure the folder exists

# Load and process each image
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

if not image_files:
    print("No images found in the folder!")
    exit()

print(f"Processing {len(image_files)} images...")

for img_file in image_files:
    img_path = image_folder / img_file
    output_path = output_folder / f"detected_{img_file}"

    # Load image
    img = Image.open(img_path)
    
    # Run detection
    results = model(img)

    # Get detections as DataFrame
    detections = results.pandas().xyxy[0]  

    # Draw bounding boxes
    draw = ImageDraw.Draw(img)
    for _, row in detections.iterrows():
        x1, y1, x2, y2 = row["xmin"], row["ymin"], row["xmax"], row["ymax"]
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

    # Save image with detections in detection_results folder
    img.save(output_path)

    print(f"\n Detections for {img_file}:\n", detections)

print("\n Detection completed! Results saved in:", output_folder)
