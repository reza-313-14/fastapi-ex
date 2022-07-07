from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from fastapi import Depends, status
from sqlalchemy.orm import Session
from database.db import get_db
from fastapi.exceptions import HTTPException
from jose.exceptions import JWTError
from database.db_user import get_user_by_username


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "17cd7bc169521e5b0f0efb9cd41472c83b747912795e3e624888e873809c5db4" # in linux : openssl rand -hex 32
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expire_delta: Optional[timedelta]= None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session= Depends(get_db)):
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid credentials', headers={"WWW-authenticate": "bearer"})
    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        
        if not username:
            raise error_credential
        
    except JWTError:
        raise error_credential
    
    
    user = get_user_by_username(username, db)
    
    return user