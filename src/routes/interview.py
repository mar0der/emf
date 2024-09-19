from flask import Blueprint, jsonify, request
from models.interview import Interview
from schemas.interview import InterviewSchema
from extensions import db
from utils.decorators import token_required

bp = Blueprint('interview_routes', __name__, url_prefix='/v1/interviews')

@bp.route('', methods=['POST'])
@token_required
def create_interview():
    data = InterviewSchema.load(request.json)
    new_interview = Interview(**data)
    db.session.add(new_interview)
    db.session.commit()
    return jsonify(InterviewSchema.dump(new_interview)), 201

@bp.route('', methods=['GET'])
@token_required
def get_interviews():
    interviews = Interview.query.all()
    return jsonify([InterviewSchema.dump(interview) for interview in interviews])

@bp.route('/<int:interview_id>', methods=['GET'])
@token_required
def get_interview(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    return jsonify(InterviewSchema.dump(interview))

@bp.route('/<int:interview_id>', methods=['PUT'])
@token_required
def update_interview(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    data = InterviewSchema.load(request.json)
    for key, value in data.items():
        setattr(interview, key, value)
    db.session.commit()
    return jsonify(InterviewSchema.dump(interview))

@bp.route('/<int:interview_id>', methods=['DELETE'])
@token_required
def delete_interview(interview_id):
    interview = Interview.query.get_or_404(interview_id)
    db.session.delete(interview)
    db.session.commit()
    return '', 204