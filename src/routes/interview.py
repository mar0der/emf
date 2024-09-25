from flask import Blueprint, jsonify, request
from models.interview import Interview
from schemas.interview import InterviewSchema
from extensions import db
from utils.decorators import token_required
from datetime import datetime

bp = Blueprint('interview_routes', __name__, url_prefix='/v1/interviews')

@bp.route('', methods=['GET'])
@token_required
def get_interviews():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    interviews = Interview.query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'interviews': [InterviewSchema.dump(interview) for interview in interviews.items],
        'total': interviews.total,
        'pages': interviews.pages,
        'current_page': page
    }), 200

@bp.route('/<int:interview_id>', methods=['GET'])
@token_required
def get_interview(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    return jsonify(InterviewSchema.dump(interview)), 200

@bp.route('/by-date', methods=['GET'])
@token_required
def get_interviews_by_date():
    date_str = request.args.get('date')
    
    if not date_str:
        return jsonify({"error": "Date parameter is required"}), 400
    
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    interviews = Interview.query.filter(Interview.date == date).all()
    
    return jsonify({
        'interviews': [InterviewSchema.dump(interview) for interview in interviews],
        'total': len(interviews),
        'date': date_str
    }), 200

@bp.route('/by_interviewer/<string:interviewer>', methods=['GET'])
@token_required
def get_interviews_by_interviewer(interviewer):
    interviews = Interview.query.filter(Interview.interviewer.ilike(f'%{interviewer}%')).all()
    return jsonify([InterviewSchema.dump(interview) for interview in interviews])