import torch
from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
MODEL_PATH = 'yolov8n.pt'  # Using YOLOv8 nano model for better efficiency
model = YOLO(MODEL_PATH)

# Function to perform animal detection
def detect_animals(image_path):
    try:
        # Perform detection
        results = model.predict(image_path)

        # Load image for visualization
        image = cv2.imread(image_path)

        # Draw bounding boxes
        for box in results[0].boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = box
            label = f"{model.names[int(cls)]} {conf:.2f}"
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the result
        output_path = f'static/detections/detected_{os.path.basename(image_path)}'
        os.makedirs('static/detections', exist_ok=True)
        cv2.imwrite(output_path, image)

        return output_path

    except Exception as e:
        print(f"Error during detection: {e}")
        return None