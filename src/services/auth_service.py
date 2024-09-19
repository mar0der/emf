from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.token import Token
from extensions import db
import secrets
from datetime import datetime, timedelta
import re

class AuthService:
    @staticmethod
    def register_user(username, email, password, confirm_password):
        if password != confirm_password:
            return None, "Passwords do not match"
        
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"
        if User.query.filter_by(email=email).first():
            return None, "Email already exists"
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user, None

    @staticmethod
    def is_password_valid(password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    @staticmethod
    def login_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return user, None
        return None, "Invalid username or password"

    @staticmethod
    def logout_user():
        logout_user()

    @staticmethod
    def generate_token(user):
        token = secrets.token_hex(32)
        new_token = Token(
            token=token,
            user_id=user.id,
            expires_at=datetime.utcnow() + timedelta(days=30)
        )
        db.session.add(new_token)
        db.session.commit()
        return new_token

    @staticmethod
    def validate_token(token):
        token_record = Token.query.filter_by(token=token).first()
        if token_record and token_record.expires_at > datetime.utcnow():
            return token_record.user
        return None