from flask import Blueprint, jsonify, request
from models.user import User
from utils.decorators import token_required

bp = Blueprint('user_routes', __name__, url_prefix='/v1/users')

@bp.route('', methods=['GET'])
@token_required
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])

@bp.route('/<int:user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "username": user.username, "email": user.email})

@bp.route('/me', methods=['GET'])
@token_required
def get_current_user():
    return jsonify({
        "id": request.current_user.id, 
        "username": request.current_user.username, 
        "email": request.current_user.email
    })