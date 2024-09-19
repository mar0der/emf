from app import create_app, db
from models.user import User
from models.interview import Interview
from models.token import Token
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
import secrets

def seed_data():
    app = create_app()
    with app.app_context():
        # Check if data already exists
        if User.query.filter_by(username='elon_fan').first() is None:
            # Create admin user
            admin_user = User(
                username='elon_fan',
                email='elon_fan@example.com',
                password=generate_password_hash('12qwaszx'),
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.flush()  # This will assign an id to admin_user

            # Create a token for the user
            token = Token(
                token=secrets.token_hex(32),
                user_id=admin_user.id,
                expires_at=datetime.utcnow() + timedelta(days=30)
            )
            db.session.add(token)

            # Create an interview
            interview = Interview(
                date=datetime.now().date(),
                interviewer="Joe Rogan",
                title="Elon Musk on AI and the Future",
                link="https://example.com/elon-musk-interview",
                platform="Spotify",
                description="Elon Musk discusses artificial intelligence and his vision for the future.",
                transcript="This is a sample transcript of the interview..."
            )
            db.session.add(interview)

            db.session.commit()
            print("Sample data added successfully.")
            print(f"Admin user created. Username: elon_fan, Password: 12qwaszx")
            print(f"API Token for elon_fan: {token.token}")
        else:
            print("Data already exists. Skipping seed.")

if __name__ == "__main__":
    seed_data()