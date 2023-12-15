import sqlalchemy
from sqlalchemy.sql.expression import null
from database import Base, engine
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

import enum

from utils import PLACE_CATEGORY, FRIEND_STATUS

place_category = enum.Enum('Place_Category', {field: field for field in PLACE_CATEGORY}, type=str)
friend_status = enum.Enum('Friend_Status', {field: field for field in FRIEND_STATUS}, type=str)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 
    active = Column(Boolean(default=True))
    
    places = relationship('Place', back_populates='user')
    source_friendships = relationship('Friend', back_populates='source_friend', foreign_keys='Friend.source_friend_id')
    target_friendships = relationship('Friend', back_populates='target_friend', foreign_keys='Friend.target_friend_id')
    tags = relationship('Tag', back_populates='user')

    
class Place(Base):
    __tablename__ = 'place'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(Text)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 
    active = Column(Boolean(default=True))
    
    user = relationship('User', back_populates='place')
    tags = relationship('Tag', back_populates='place')
    categories = relationship('Category', back_populates='place')
    
    
class Friend(Base):
    __tablename__ = 'friend'
    
    id = Column(Integer, primary_key=True)
    source_friend_id = Column(Integer, ForeignKey('user.id'))   
    target_friend_id = Column(Integer, ForeignKey('user.id')) 
    status = Column(sqlalchemy.Enum(friend_status))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 
    active = Column(Boolean(default=True))
    
    source_friend = relationship('User', foreign_keys=[source_friend_id], back_populates='source_friendships')
    target_friend = relationship('User', foreign_keys=[target_friend_id], back_populates='target_friendships')
    categories = relationship('Category', back_populates='place')
    
class Tag(Base):
    __tablename__ = 'tag'
    
    id = Column(Integer, primary_key=True)
    place_id = Column(Integer, ForeignKey('place.id'))
    friend_id = Column(Integer, ForeignKey('user.id')) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 
    friend_notification = Column(Boolean(default=False))
    liked = Column(Boolean(default=False))
    active = Column(Boolean(default=True))
    
    place = relationship('Place', back_populates='tag')
    friend = relationship('User', back_populates='tag')
    
class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    place_id = Column(Integer, ForeignKey('place.id'))
    category = Column(sqlalchemy.Enum(place_category))
    active = Column(Boolean(default=True))
    
    place = relationship('Place', back_populates='categories')
    
    
    
    
    

