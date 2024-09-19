import os
from flask import Flask, jsonify, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from extensions import db
from config import Config
from models.interview import Interview
from models.user import User
from models.prediction import Prediction
from models.interview_prediction import InterviewPrediction

login_manager = LoginManager()

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))
    
def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)
    
    admin = Admin(app, name='Elon Musk Interviews Admin', template_mode='bootstrap3', index_view=SecureAdminIndexView())
    admin.add_link(MenuLink(name='Back to Dashboard', url='/dashboard'))
    admin.add_view(SecureModelView(Interview, db.session))
    admin.add_view(SecureModelView(User, db.session))
    admin.add_view(SecureModelView(Prediction, db.session))
    admin.add_view(SecureModelView(InterviewPrediction, db.session))

    with app.app_context():
        db.create_all()
        from routes.auth import bp as auth_bp
        from routes.user import bp as user_bp
        from routes.interview import bp as interview_bp
        from routes.web_routes import bp as web_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(interview_bp)
        app.register_blueprint(web_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)