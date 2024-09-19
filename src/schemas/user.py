from typing import Dict, Any

class UserSchema:
    @staticmethod
    def dump(user) -> Dict[str, Any]:
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at.isoformat() if user.created_at else None
        }

    @staticmethod
    def load(data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'username': data.get('username'),
            'email': data.get('email')
        }