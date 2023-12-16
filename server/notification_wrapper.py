from models import *
from typing import Union, Literal
import json

class NotificationRoute():
    def __init__(self, session, user_id: int, request: Union[dict, str]):
        self.session = session
        self.user_id = user_id
        
        if isinstance(request, str):
            request = json.loads(request)
        self.task = request.get("task", None)
        self.content = request.get("content", None)
        
    def response(self):
        if self.task == "view_notification_list":
            success, code, content = self.view_notification()
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
            
    def view_notification(self):
        success = True
        code = 140
        content = []
        notification = self.session.query(Tag.id, Place.id, Place.name, User.id, User.username, 
                                        Tag.created_at, Tag.friend_notification) \
                                    .join(Place, Tag.place_id == Place.id) \
                                    .join(User, Place.user_id == User.id) \
                                    .filter(Tag.friend_id == self.user_id,
                                            Tag.active).all()      
        for tag_id, place_id, place_name, user_id, username, created_at, friend_notification in notification:
            content.append({"place_id": place_id, "place_name": place_name,
                            "user_id": user_id, "username": username,
                            "created_at": created_at.strftime("%m/%d/%Y, %H:%M:%S"), "read": friend_notification})
            
        return success, code, content