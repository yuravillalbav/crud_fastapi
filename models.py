from sqlalchemy import Column, Integer, String
from database import Base

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    author = Column(String(50))
    age = Column(Integer)