from flask import Blueprint, request, jsonify
from backend.detection.model import AnimalDetectionModel  # Correct model import

# Blueprint Setup
detection_bp = Blueprint('detection', __name__)
model = AnimalDetectionModel("model/best.pt")  # Use your trained YOLOv5 model

@detection_bp.route('/detect', methods=['POST'])
def detect_animals():
    # Ensure the request contains the image file
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    # Save uploaded image temporarily
    image_file = request.files['image']
    image_path = f"/tmp/{image_file.filename}"
    image_file.save(image_path)

    # Perform detection
    try:
        detections = model.detect_animals(image_path)
        return jsonify({'detections': detections})
    except Exception as e:
        return jsonify({'error': f'Detection failed: {str(e)}'}), 500
