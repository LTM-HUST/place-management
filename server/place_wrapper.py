from models import *
from typing import Union
import json

from session import get_user_from_session_id
from sqlalchemy.orm import joinedload


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
            success, code, content = self.view_place_detail()
        elif self.task == "view_categories":
            success, code, content = self.view_categories()
        elif self.task == "create_place":
            self.name = self.content.get("name", None)
            self.address = self.content.get("address", None)
            self.tags = self.content.get("tags", None)
            self.tagged_friends = self.content.get("tagged_friends", None)
            self.description = self.content.get("description", None)
            success, code, content = self.create_place()
        elif self.task == "update_place":
            pass
        elif self.task == "delete_place":
            self.place_id = self.content.get("id", None)
            success, code, content = self.delete_place()
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
            .join(Tag, Place.tag) \
            .filter(Tag.friend_id == self.user.id, Tag.liked, Tag.active, Place.active).all()
        places = my_places + liked_places
        for place in places:
            content.append({
                "id": place.id,
                "name": place.name,
                "description": place.description
            })

        return success, code, content

    @get_user_from_session_id
    def view_my_places(self):
        success = True
        code = 111
        content = []

        places = self.session.query(Place.id, Place.name, Place.description) \
            .filter(Place.user_id == self.user.id, Place.active).all()
        for place in places:
            content.append({
                "id": place.id,
                "name": place.name,
                "description": place.description
            })

        return success, code, content

    @get_user_from_session_id
    def view_liked_places(self):
        success = True
        code = 112
        content = []

        places = self.session.query(Place.id, Place.name, Place.description) \
            .join(Tag, Place.tag) \
            .filter(Tag.friend_id == self.user.id, Tag.liked, Tag.active, Place.active).all()
        for place in places:
            content.append({
                "id": place.id,
                "name": place.name,
                "description": place.description
            })

        return success, code, content

    @get_user_from_session_id
    def view_place_detail(self):
        place = self.session.query(Place).options(
            joinedload(Place.tag), joinedload(Place.category)
        ).filter(Place.id == self.id, Place.active).first()

        categories = [{"id": category.id, "category": category.category} for category in place.category]
        tagged_friends = []
        for tag in place.tag:
            friend_id = tag.friend_id
            friend_as_user = self.session.query(User).filter(User.id == friend_id, User.active).first()
            tagged_friends.append({
                "id": friend_as_user.id,
                "username": friend_as_user.username
            })

        if place:
            success = True
            code = 113
            content = {
                "id": place.id,
                "name": place.name,
                "address": place.address,
                "description": place.description,
                "categories": categories,
                "tagged_friends": tagged_friends
            }
        else:
            success = False
            code = 216
            content = {}

        return success, code, content

    def view_categories(self):
        success = True
        code = 160
        content = []

        categories = [category for category in place_category.__members__.values()]
        for id, category in enumerate(categories):
            content.append({
                "id": id,
                "category": category
            })

        return success, code, content

    @get_user_from_session_id
    def create_place(self):
        content = {}

        if not self.name:
            success = False
            code = 214
            return success, code, content

        place = Place(
            name=self.name,
            address=self.address,
            description=self.description,
            user_id=self.user.id
        )
        for category_id in self.tags:
            category = Category(category=place_category.__members__.get(category_id))
            place.category.append(category)
        for friend_id in self.tagged_friends:
            tag = Tag(friend_id=friend_id)
            place.tag.append(tag)

        self.session.add(place)
        self.session.commit()
        success = True
        code = 114

        return success, code, content
    
    @get_user_from_session_id
    def delete_place(self):
        content = {}

        place = self.session.query(Place).filter(Place.id == self.place_id, Place.user_id == self.user.id).first()
        place.active = False
        self.session.commit()

        success = True
        code = 116

        return success, code, content
