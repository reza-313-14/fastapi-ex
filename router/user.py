from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from database import db_user
from database.db import get_db

router = APIRouter(prefix='/user', tags=['user'])


# create user
@router.post('/', response_model=UserDisplay)
def create_user(user:UserBase, db=Depends(get_db)):
    return db_user.create_user(db, user)


# read user



# update user



# delete user