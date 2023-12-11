from flask import Blueprint, request, jsonify
from .email_service import send_email, receive_email

email_bp = Blueprint('email_bp', __name__)

@email_bp.route('/send', methods=['POST'])
def send():
    data = request.json
    send_email(data['sender'], data['recipient'], data['subject'], data['body'])
    return jsonify({"message": "Email sent successfully"}), 200

@email_bp.route('/receive', methods=['GET'])
def receive():
    emails = receive_email()
    return jsonify(emails), 200
