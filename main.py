from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional


app = FastAPI()

# first
@app.get('/')
def home():
    return {"name": 'mahdi'}

# path arguments
@app.get('/blog/{id}')
def blog(id: int):
    return {"message": f"blog id is {id}"}

# custom type
class BlogType(str, Enum):
    type1 = 'food'
    type2 = 'car'
    type3 = 'programming'


@app.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {'message': f'blog type is {type=}'}

# custom status
@app.get('/blog', status_code = status.HTTP_200_OK)
def GetBlog(page:int, response:Response):
    if page > 20:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'page is {page=}'}
    
# default value
@app.get('/blog/')
def get_page(page:Optional[int]=1, number:int=None):
    return {'message': f'{page=} and {number=}'}