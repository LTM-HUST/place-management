from models import *
from typing import Union, Literal
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
            success, code, content = self.send_friend_request()
        elif self.task == "accept_friend_request":
            self.friend_id = self.content.get("source_friend_id", None)
            success, code, content = self.task_friend_request(type="accepted")
        elif self.task == "reject_friend_request":
            self.friend_id = self.content.get("source_friend_id", None)
            success, code, content = self.task_friend_request(type="rejected")
        elif self.task == "delete_friend":
            self.friend_id = self.content.get("friend_id", None)
            success, code, content = self.delete_friend()
        elif self.task == "view_friend_list":
            success, code, content = self.view_friend()
        elif self.task == "view_friend_request":
            success, code, content = self.view_friend_request()
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
        
    def send_friend_request(self):
        content = {}
        if not self.validate_friend():
            success = False
            code = 206
        elif self.find_relationship():
            success = False
            code = 220
        else:
            friend = Friend(source_friend_id=self.user_id, target_friend_id=self.friend_id, status="waiting")

            self.session.add(friend)
            self.session.commit()
            
            success = True
            code = 120 
            
        return success, code, content  
    
    def task_friend_request(self, type: Literal["accepted", "rejected"]):
        content = {}
        if not self.validate_friend():
            success = False
            code = 206
        else:
            if self.update_request(type):  
                success = True
                code = 122 if type == "accepted" else 123
            else:
                success = False
                code = 221
        return success, code, content 
    
    def delete_friend(self):
        content = {}
        if not self.validate_friend():
            success = False
            code = 206 
        friendship = self.find_relationship()
        if not friendship:
            success = False
            code = 224
        else:
            friendship.active = False
            self.session.commit()
            
            success = True
            code = 124
        return success, code, content
    
    def view_friend(self):
        success = True
        code = 130
        friend_source = self.session.query(Friend.target_friend_id, User.username) \
                                    .join(User, Friend.target_friend_id == User.id) \
                                    .filter(Friend.source_friend_id == self.user_id, 
                                            Friend.active, 
                                            Friend.status == "accepted").all()
        friend_target = self.session.query(Friend.source_friend_id, User.username) \
                                    .join(User, Friend.source_friend_id == User.id) \
                                    .filter(Friend.target_friend_id == self.user_id, 
                                            Friend.active, 
                                            Friend.status == "accepted").all()
        friend_list = friend_source + friend_target
        content = []
        for id, username in friend_list:
            content.append({"id": id, "username": username})
            
        return success, code, content
    
    def view_friend_request(self):
        success = True
        code = 131
        friend_request = self.session.query(Friend.source_friend_id, User.username) \
                                    .join(User, Friend.source_friend_id == User.id) \
                                    .filter(Friend.target_friend_id == self.user_id, 
                                            Friend.active, 
                                            Friend.status == "waiting").all()
        content = []
        for id, username in friend_request:
            content.append({"id": id, "username": username})
            
        return success, code, content

    # Check if user exists or not
    def validate_friend(self):
        if self.session.query(User).filter(User.id == self.friend_id, User.active) is None:
            return False
        return True
    
    # Check if user in friend list or not
    def find_relationship(self):
        friend_source = self.session.query(Friend) \
                                    .filter(Friend.target_friend_id == self.friend_id, 
                                            Friend.source_friend_id == self.user_id, 
                                            Friend.active,
                                            Friend.status == "accepted").first()
        if friend_source:
            return friend_source
        
        friend_target =  self.session.query(Friend) \
                                    .filter(Friend.source_friend_id == self.friend_id, 
                                            Friend.target_friend_id == self.user_id, 
                                            Friend.active,
                                            Friend.status == "accepted").first()
        if friend_target:
            return friend_target
        
        return None
    
    # Check if user in friend request or not
    def update_request(self, type: Literal["accepted", "rejected"]):
        friend = self.session.query(Friend) \
                            .filter(Friend.source_friend_id == self.friend_id, 
                                    Friend.target_friend_id == self.user_id, 
                                    Friend.active, 
                                    Friend.status == "waiting").first() 
        if friend:
            friend.status = type
            self.session.commit()  
            return True
        return False
    
    
        