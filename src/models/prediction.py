from extensions import db
from datetime import datetime

class Prediction(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(500), nullable=False)
    goal_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('in_progress', 'achieved', 'canceled', 'missed', name='prediction_status'), default='in_progress')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    interviews = db.relationship('Interview', secondary='interview_predictions', back_populates='predictions')

    def __repr__(self):
        return f'<Prediction {self.id}: {self.goal[:30]}...>'