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


def get_all_users(db:Session):
    return db.query(DbUsers).all()


def get_user(id, db:Session):
    return db.query(DbUsers).filter(DbUsers.id == id).first()


def delete_user(id, db:Session):
    user = get_user(id, db)
    db.delete(user)
    db.commit()
    return {'message': 'ok'}


def update_user(id, db:Session, request:UserBase):
    user = db.query(DbUsers).filter(DbUsers.id == id)
    user.update({
        DbUsers.username: request.username,
        DbUsers.email: request.email,
        DbUsers.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return {'message': 'ok'}