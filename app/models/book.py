from app.core.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    publication_date = Column(String)
    isbn = Column(String)
    description = Column(String)
    thumbnail_url = Column(String)
    bookmarks = relationship('Bookmark', backref='book')
    audiobooks = relationship('Audiobook', backref='book')
