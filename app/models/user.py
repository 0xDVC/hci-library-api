from app.core.db import Base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    preferences = Column(JSON, default={})
    bookmarks = relationship('Bookmark', backref='user')