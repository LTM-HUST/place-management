from models import *
from typing import Union 
import json

class FriendRoute():
    def __init__(self, session, user_id: int, request: Union[dict, str]):
        self.session = session
        self.user_id = user_id
        
        if isinstance(request, str):
            request = json.loads(request)
        self.task = request.get("task", None)
        self.content = request.get("content", None)
        
    def response(self):
        if self.task == "send_friend_request":
            self.friend_id = self.content.get("target_friend_id", None)
            res = self.send_friend_request()
        else:
            res = {
                "success": False,
                "code": 300,
                "content": {}
            }
            
        return res       
        
    def send_friend_request(self):
        content = {}
        if not self.validate_friend():
            success = False
            code = 206
        elif self.validate_relationship():
            success = False
            code = 220
        else:
            friend = Friend(source_friend_id=self.user_id, target_friend_id=self.friend_id, status="waiting")

            self.session.add(friend)
            self.session.commit()
            
            success = True
            code = 120 
        response = {
            "success": success,
            "code": code,
            "content": content
        }
        return response       

    def validate_friend(self):
        if self.session.query(User).filter(User.id == self.friend_id, User.active) is None:
            return False
        return True
    
    def validate_relationship(self):
        if self.session.query(Friend).filter(Friend.source_friend_id == self.friend_id, Friend.target_friend_id == self.user_id, Friend.active).all():
            return True
        if self.session.query(Friend).filter(Friend.target_friend_id == self.friend_id, Friend.source_friend_id == self.user_id, Friend.active).all():
            return True
        return False
        