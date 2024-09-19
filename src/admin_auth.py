from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from services.auth_service import AuthService

bp = Blueprint('admin_auth', __name__, url_prefix='/admin')

@bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user, error = AuthService.login_user(request.form['username'], request.form['password'])
        if error:
            flash(error)
        elif user.is_admin:
            return redirect(url_for('admin.index'))
        else:
            flash('You do not have admin privileges')
    return render_template('admin/login.html')

@bp.route('/logout')
@login_required
def admin_logout():
    AuthService.logout_user()
    return redirect(url_for('admin_auth.admin_login'))