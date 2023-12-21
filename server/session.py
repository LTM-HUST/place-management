import uuid

from models import User


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = None
        return session_id

    def get_user_ids(self):
        return self.sessions.values()

    def get_user_id(self, session_id):
        return self.sessions[session_id]

    def modify_session(self, session_id, user_id):
        self.sessions[session_id] = user_id

    def delete_session(self, session_id):
        del self.sessions[session_id]


def get_user_from_session_id(func):
    def wrapper(self, *args, **kw):
        user_id = session_manager.get_user_id(self.session_id)
        if user_id is None:
            success = False
            code = 205
            content = {}
            return success, code, content
        self.user = self.session.query(User).filter(User.id == user_id).first()
        if not self.user:
            success = False
            code = 206
            content = {}
            return success, code, content
        return func(self, *args, **kw)
    return wrapper


session_manager = SessionManager()
