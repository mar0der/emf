from extensions import db
from datetime import datetime

class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    interviewer = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(500), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    transcript = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    predictions = db.relationship('Prediction', secondary='interview_prediction', back_populates='interviews')

    def __repr__(self):
        return f'<Interview {self.title} on {self.date}>'