from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from database import db_user
from database.db import get_db
from typing import Optional, List, Dict

router = APIRouter(prefix='/user', tags=['user'])


# create user
@router.post('/', response_model=UserDisplay)
def create_user(user:UserBase, db=Depends(get_db)):
    return db_user.create_user(db, user)


# read all users
@router.get('/users', response_model=List[UserDisplay])
def get_all_users(db=Depends(get_db)):
    return db_user.get_all_users(db)


# read user
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db=Depends(get_db)):
    return db_user.get_user(id, db)


# update user
@router.post('/update/{id}')
def update_user(id: int, user: UserBase, db=Depends(get_db)):
    return db_user.update_user(id, db, user)


# delete user
@router.get('/delete/{id}')
def delete_user(id: int, db=Depends(get_db)):
    return db_user.delete_user(id, db)
