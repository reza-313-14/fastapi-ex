from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional


router = APIRouter(prefix='/blog/post', tags=['posts'])

class BlogModel(BaseModel):
    title:str
    content:str
    nb_command: int
    published:Optional[bool]


@router.post('/new/{id}')
def create_blog(blog:BlogModel, id:int=Path(None, gt=2), version:int=None):
    return {'message': 'hello world', 'id': id, "version": version}

"""

gt = great than 
ge = great or equal
lt = less than
le = less or equal

"""


@router.post('/new/{id}/comment')
def create_comment(id:str=Path(None, alias='id parameters', title='hello mahdi', description='for id', min_length=6), blog: BlogModel=None, comment_id: int = Query(None, title='title text', description='description text', alias='test', deprecated=True)):
    return {'message': f"{id=}, {blog=}, {comment_id=}"}