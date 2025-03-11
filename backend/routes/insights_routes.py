from flask import Blueprint, jsonify
from database.data_handler import get_all_records

insights_bp = Blueprint('insights', __name__)

@insights_bp.route('/records', methods=['GET'])
def get_records():
    records = get_all_records()
    return jsonify({'records': records})
