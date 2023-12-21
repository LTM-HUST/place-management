from models import *
from typing import Union
import json

from session import session_manager, get_user_from_session_id


class UserRoute():

    def __init__(self, session, session_id, request: Union[dict, str]):
        self.session = session
        self.session_id = session_id

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

        if not (self.username and self.password and self.retype_password):
            success = False
            code = 214
        elif self.username_exist():
            success = False
            code = 201
        elif self.password != self.retype_password:
            success = False
            code = 203
        else:
            user = User(username=self.username, password=self.password)
            self.session.add(user)
            self.session.commit()
            success = True
            code = 100

        return success, code, content

    def login(self):
        content = {}
        user_id = self.get_user_id_from_login_info()

        if not user_id:
            success = False
            code = 202
        elif user_id in session_manager.get_user_ids():
            success = False
            code = 204
        else:
            session_manager.modify_session(self.session_id, user_id)
            success = True
            code = 101

        return success, code, content

    def logout(self):
        session_manager.modify_session(self.session_id, None)

        success = True
        code = 102
        content = {}

        return success, code, content

    @get_user_from_session_id
    def view_profile(self):
        username = self.user.username

        success = True
        code = 150
        content = {
            "username": username
        }

        return success, code, content

    @get_user_from_session_id
    def change_password(self):
        content = {}

        if self.new_password != self.retype_password:
            success = False
            code = 203
        else:
            self.user.password = self.new_password
            self.session.commit()
            success = True
            code = 103

        return success, code, content

    def username_exist(self) -> bool:
        return self.session.query(User).filter(User.username == self.username).first() is not None
    
    def get_user_id_from_login_info(self) -> int:
        user = self.session.query(User.id).filter(User.username == self.username, User.password == self.password).first()
        return user.id if user else None
