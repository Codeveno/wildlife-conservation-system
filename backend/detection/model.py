import torch
from yolov5.models.common import DetectMultiBackend
import cv2

class YOLOv5Model:
    def __init__(self):
        model_path = "model/best.pt"
        self.model = DetectMultiBackend(model_path, device='cpu')
        print(f"✅ Model loaded successfully from: {model_path}")

    def detect_animals(self, image_path):
        try:
            img = cv2.imread(image_path)  # Read image
            results = self.model(img)
            return results.pandas().xyxy[0].to_dict(orient='records')
        except Exception as e:
            print(f"❌ Detection error: {e}")
            return {"error": "Detection process failed."}
