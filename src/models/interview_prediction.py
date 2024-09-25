from extensions import db

class InterviewPrediction(db.Model):
    __tablename__ = 'interview_predictions'

    id = db.Column(db.Integer, primary_key=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id'), nullable=False)
    prediction_id = db.Column(db.Integer, db.ForeignKey('predictions.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint('interview_id', 'prediction_id', name='unique_interview_prediction'),)

    def __repr__(self):
        return f'<InterviewPrediction {self.interview_id}-{self.prediction_id}>'