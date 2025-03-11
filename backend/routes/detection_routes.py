from flask import Blueprint, request, jsonify
from backend.detection.model import YOLOv5Model


detection_bp = Blueprint('detection', __name__)
model = YOLOv5Model()

@detection_bp.route('/detect', methods=['POST'])
def detect_animals():
    image_path = request.form['image_path']
    detections = model.detect_animals(image_path)
    return jsonify({'detections': detections})
