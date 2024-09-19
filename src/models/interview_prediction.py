from extensions import db

class InterviewPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('interview.id'), nullable=False)
    prediction_id = db.Column(db.Integer, db.ForeignKey('prediction.id'), nullable=False)
    prediction_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<InterviewPrediction {self.interview_id}-{self.prediction_id}>'