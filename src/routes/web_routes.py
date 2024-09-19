from flask import Blueprint, redirect, url_for
from flask_login import current_user

bp = Blueprint('web', __name__)

@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return redirect(url_for('auth.login'))