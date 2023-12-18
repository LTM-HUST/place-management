from models import *
from typing import Union
import json

from session import session_manager

class UserRoute():

    def __init__(self, session, session_id, request: Union[dict, str]):
        self.session = session
        self.session_id = "01bf1e6a-1e1d-4242-9b8a-878267507983"

        if isinstance(request, str):
            request = json.loads(request)
        self.task = request.get("task", None)
        self.content = request.get("content", None)

    def response(self):
        if self.task == "register":
            self.username = self.content.get("username", None)
            self.password = self.content.get("password", None)
            self.retype_password = self.content.get("retype_password", None)
            success, code, content = self.register()
        elif self.task == "login":
            self.username = self.content.get("username", None)
            self.password = self.content.get("password", None)
            success, code, content = self.login()
        elif self.task == "logout":
            success, code, content = self.logout()
        elif self.task == "view_profile":
            success, code, content = self.view_profile()
        elif self.task == "change_password":
            self.old_password = self.content.get("old_password", None)
            self.new_password = self.content.get("new_password", None)
            self.retype_password = self.content.get("retype_password", None)
            success, code, content = self.change_password()
        else:
            success = False
            code = 300
            content = {}

        res = {
            "success": success,
            "code": code,
            "content": content
        }
        return res

    def register(self):
        content = {}

        if self.username_exist():
            success = False
            code = 201
        elif self.password != self.retype_password:
            success = False
            code = 203
        elif not (self.username and self.password and self.retype_password):
            success = False
            code = 214
        else:
            user = User(username=self.username, password=self.password)
            self.session.add(user)
            self.session.commit()

            success = True
            code = 100

        return success, code, content

    def login(self):
        content = {}
        user_id = self.get_user_id()

        if not user_id:
            success = False
            code = 202
        elif user_id in session_manager.get_user_ids():
            success = False
            code = 204
        else:
            session_id = session_manager.create_session(user_id)

            success = True
            code = 101
            content = {
                "session_id": session_id
            }

        return success, code, content

    def logout(self):
        session_manager.delete_session(self.session_id)

        success = True
        code = 102
        content = {}

        return success, code, content

    def view_profile(self):
        username = self.get_user_from_session().username

        success = True
        code = 150
        content = {
            "username": username
        }

        return success, code, content

    def change_password(self):
        content = {}

        if self.new_password != self.retype_password:
            success = False
            code = 203
        else:
            user = self.get_user_from_session()
            user.password = self.new_password
            self.session.commit()
            success = True
            code = 103

        return success, code, content

    def username_exist(self) -> bool:
        return self.session.query(User).filter(User.username == self.username).first() is not None

    def get_user_from_session(self) -> User:
        return self.session.query(User).filter(User.id == session_manager.get_user_id(self.session_id)).first()
    
    def get_user_id(self) -> int:
        return self.session.query(User.id).filter(User.username == self.username).first()

