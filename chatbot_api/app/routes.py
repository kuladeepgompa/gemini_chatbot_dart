from flask import Blueprint, request, jsonify
from app.services.gemini_service import GeminiService
from app.services.error_handling import handle_errors
from app.config import Config

api = Blueprint('api', __name__)
gemini_service = GeminiService()

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@api.route('/chat', methods=['POST'])
@handle_errors
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        raise ValueError("Missing 'message' in request body")

    response = gemini_service.generate_response(data['message'])
    return jsonify(response)
