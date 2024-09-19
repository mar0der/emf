from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from services.auth_service import AuthService

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user, error = AuthService.register_user(
            request.form['username'], 
            request.form['email'], 
            request.form['password'],
            request.form['confirm_password']
        )
        if error:
            flash(error, 'danger')
            return render_template('register.html', form_data=request.form)
        
        login_user(user)
        flash("User created successfully. You are now logged in.", 'success')
        return redirect(url_for('auth.dashboard'))
    
    return render_template('register.html', form_data={})

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        user, error = AuthService.login_user(request.form['username'], request.form['password'])
        if error:
            flash(error, 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        flash("Logged in successfully", 'success')
        return redirect(url_for('auth.dashboard'))
    
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/generate_token', methods=['POST'])
@login_required
def generate_token():
    token = AuthService.generate_token(current_user)
    flash(f'Your new API token is: {token.token}', 'info')
    return redirect(url_for('auth.dashboard'))