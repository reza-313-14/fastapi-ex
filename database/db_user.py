from sqlalchemy.orm.session import Session
from schemas import UserBase
from database.models import DbUsers
from database.hash import Hash

def create_user(db:Session, request:UserBase):
    user = DbUsers(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user