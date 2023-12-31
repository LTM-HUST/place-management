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
            self.id = self.content.get("id", None)
            self.name = self.content.get("name", None)
            self.address = self.content.get("address", None)
            self.tags = self.content.get("tags", None)
            self.tagged_friends = self.content.get("tagged_friends", None)
            self.description = self.content.get("description", None)
            success, code, content = self.update_place()
        elif self.task == "delete_place":
            self.id = self.content.get("id", None)
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

        my_places = self.get_my_places()
        liked_places = self.get_liked_places()
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

        places = self.get_my_places()
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

        places = self.get_liked_places()
        for place in places:
            content.append({
                "id": place.id,
                "name": place.name,
                "description": place.description
            })

        return success, code, content

    @get_user_from_session_id
    def view_place_detail(self):
        place = (
            self.session.query(Place)
            .options(joinedload(Place.category), joinedload(Place.tag))
            .filter(Place.id == self.id, Place.active)
            .first()
        )
        categories = [category.category for category in place.category if category.active]
        tagged_friends = []
        for tag in place.tag:
            if not tag.active:
                continue
            friend_as_user = (
                self.session.query(User)
                .filter(User.id == tag.friend_id, User.active).first()
            )
            if friend_as_user:
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

        for category in place_category:
            content.append(category)

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
        for category_name in self.tags:
            category = Category(category=place_category(category_name))
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
    def update_place(self):
        content = {}

        place = self.session.query(Place).filter(Place.id == self.id, Place.user_id == self.user.id).first()
        place.name = self.name
        place.address = self.address
        place.description = self.description

        old_categories = [category.category for category in place.category]
        new_categories = self.tags
        for category in [category for category in old_categories if category not in new_categories]:
            category = self.session.query(Category).filter(Category.place_id == self.id, Category.category == category).first()
            category.active = False
        for category in [category for category in new_categories if category not in old_categories]:
            category = Category(category=category)
            place.category.append(category)

        old_tagged_friends_id = [tag.friend_id for tag in place.tag]
        new_tagged_friends_id = self.tagged_friends
        for friend_id in [id for id in new_tagged_friends_id if id not in old_tagged_friends_id]:
            tag = Tag(friend_id=friend_id)
            place.tag.append(tag)

        self.session.commit()
        success = True
        code = 115

        return success, code, content

    @get_user_from_session_id
    def delete_place(self):
        content = {}

        place = self.session.query(Place).filter(Place.id == self.id, Place.user_id == self.user.id).first()
        place.active = False
        self.session.commit()

        success = True
        code = 116

        return success, code, content

    def get_my_places(self) -> list[Place]:
        return (
            self.session.query(Place.id, Place.name, Place.description)
            .filter(Place.user_id == self.user.id, Place.active).all()
        )

    def get_liked_places(self) -> list[Place]:
        return (
            self.session.query(Place.id, Place.name, Place.description)
            .join(Tag, Place.tag)
            .filter(Tag.friend_id == self.user.id, Tag.liked, Tag.active, Place.active).all()
        )
