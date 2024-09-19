from typing import Dict, Any
from datetime import datetime

class InterviewSchema:
    @staticmethod
    def dump(interview) -> Dict[str, Any]:
        return {
            'id': interview.id,
            'date': interview.date.isoformat(),
            'interviewer': interview.interviewer,
            'title': interview.title,
            'link': interview.link,
            'platform': interview.platform,
            'description': interview.description,
            'created_at': interview.created_at.isoformat(),
            'updated_at': interview.updated_at.isoformat()
        }

    @staticmethod
    def load(data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'date': datetime.fromisoformat(data['date']).date(),
            'interviewer': data['interviewer'],
            'title': data['title'],
            'link': data['link'],
            'platform': data['platform'],
            'description': data.get('description')
        }