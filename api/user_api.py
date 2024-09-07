# api/user_api.py
from flask import Blueprint, request, jsonify
from service.user_service import register_user, login_user

user_api = Blueprint('user_api', __name__)

# Register API
@user_api.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    response = register_user(data)
    return jsonify(response)

# Login API
@user_api.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    response = login_user(data)
    return jsonify(response)
