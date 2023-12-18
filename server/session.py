import uuid


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = user_id
        return session_id

    def get_user_ids(self):
        return self.sessions.values()

    def get_user_id(self, session_id):
        return self.sessions.get(session_id)

    def delete_session(self, session_id):
        self.sessions.pop(session_id, None)


session_manager = SessionManager()
session_manager.sessions["01bf1e6a-1e1d-4242-9b8a-878267507983"] = '128'
