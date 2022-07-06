from database.db import Base
from sqlalchemy import Column, Integer, String

 

class DbUsers(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, index=True)
    username = Column('username', String)
    email = Column('email', String)
    password = Column('password', String)