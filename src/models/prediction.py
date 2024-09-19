from extensions import db
from datetime import datetime

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    resolution_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum('pending', 'correct', 'incorrect', name='prediction_status'), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    interviews = db.relationship('Interview', secondary='interview_prediction', back_populates='predictions')

    __table_args__ = (db.UniqueConstraint('content', 'resolution_date', name='unique_prediction'),)

    def __repr__(self):
        return f'<Prediction {self.id}: {self.content[:30]}...>'