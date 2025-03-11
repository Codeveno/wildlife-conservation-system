from flask import Blueprint, jsonify, request
from detection.tracker import DeepSORTTracker

tracking_bp = Blueprint('tracking', __name__)
tracker = DeepSORTTracker()

@tracking_bp.route('/track', methods=['POST'])
def track_objects():
    detections = request.json['detections']
    tracked_objects = tracker.track_objects(detections)
    return jsonify({'tracked_objects': tracked_objects})
