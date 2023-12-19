import uuid

from models import User


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = None
        return session_id

    def get_user_id(self, session_id):
        return self.sessions[session_id]

    def modify_session(self, session_id, user_id):
        self.sessions[session_id] = user_id

    def delete_session(self, session_id):
        self.sessions.pop(session_id, None)


def get_user_from_session_id(func):
    def wrapper(self):
        user_id = session_manager.get_user_id(self.session_id)
        if user_id is None:
            return {
                "success": False,
                "code": 205,
                "content": {}
            }
        self.user = self.session.query(User).filter(User.id == user_id).first()
        if not self.user:
            return {
                "success": False,
                "code": 206,
                "content": {}
            }
        return func(self)
    return wrapper


session_manager = SessionManager()
session_manager.sessions["01bf1e6a-1e1d-4242-9b8a-878267507983"] = '128' # TODO: remove this line after testing
