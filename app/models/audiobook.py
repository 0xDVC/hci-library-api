from app.core.db import Base 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Audiobook(Base):
    __tablename__ = 'audiobooks'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    audio_file_url = Column(String)
    book = relationship('Book', backref='audiobooks')