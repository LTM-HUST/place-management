from models import *
from typing import Union
import json

from session import session_manager, get_user_from_session_id


class PlaceRoute():

    def __init__(self, session, session_id, request: Union[dict, str]):
        self.session = session
        self.session_id = session_id

        if isinstance(request, str):
            request = json.loads(request)
        self.task = request.get("task", None)
        self.content = request.get("content", None)

    def response(self):
        if self.task == "view_places":
            success, code, content = self.view_places()
        elif self.task == "view_my_places":
            success, code, content = self.view_my_places()
        elif self.task == "view_liked_places":
            success, code, content = self.view_liked_places()
        elif self.task == "view_place_detail":
            self.id = self.content.get("id", None)
            success, code, content = self.view_place_detail(self.id)
        elif self.task == "create_place":
            pass
        elif self.task == "update_place":
            pass
        elif self.task == "delete_place":
            pass
        elif self.task == "like_friend_place":
            pass
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

    @get_user_from_session_id
    def view_places(self):
        success = True
        code = 110
        content = []

        my_places = self.session.query(Place.id, Place.name, Place.description) \
            .filter(Place.user_id == self.user.id, Place.active).all()
        liked_places = self.session.query(Place.id, Place.name, Place.description) \
            .join(Tag, Tag.friend_id == self.user.id) \
            .filter(Tag.liked, Place.active).all()
        places = my_places + liked_places
        for place in places:
            content.append({
                "id": place.id,
                "name": place.name,
                "description": place.description
            })
        
        return success, code, content
