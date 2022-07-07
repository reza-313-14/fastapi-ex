from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from database import db_article
from database.db import get_db
from typing import Optional, List, Dict

router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post("/", response_model=ArticleDisplay)
def create_article(article: ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, article)


# read article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db=Depends(get_db)):
    return db_article.get_article(id, db)