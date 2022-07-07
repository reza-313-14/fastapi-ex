from database.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
 

class DbUsers(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String)
    email = Column('email', String)
    password = Column('password', String)
    items = relationship('DbArticle', back_populates='user')
    
    
    
class DbArticle(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship('DbUsers', back_populates='items')