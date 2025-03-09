import torch
from yolov5 import YOLOv5
import cv2
import os

# Load YOLOv5 model
MODEL_PATH = 'yolov5s.pt'  # Assuming you're using the YOLOv5 small model
model = YOLOv5(MODEL_PATH)

# Function to perform animal detection
def detect_animals(image_path):
    try:
        # Load image
        image = cv2.imread(image_path)

        # Perform detection
        results = model.predict(image)

        # Draw bounding boxes
        for result in results.pred[0]:
            x1, y1, x2, y2, conf, cls = result.tolist()
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
