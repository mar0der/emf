from functools import wraps
from flask import request, jsonify
from models.token import Token
from datetime import datetime

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('X-API-Token')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        
        token_record = Token.query.filter_by(token=token).first()
        if not token_record or token_record.expires_at < datetime.utcnow():
            return jsonify({"message": "Token is invalid or expired!"}), 401
        
        request.current_user = token_record.user
        return f(*args, **kwargs)
    return decorated