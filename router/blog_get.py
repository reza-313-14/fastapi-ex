from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional
from fastapi import BackgroundTasks


router = APIRouter(prefix="/blog", tags=['blog'])


# path arguments
@router.get('/blog/{id}', tags=['home', 'test'])
def blog(id: int):
    
    """
    
    id: this is a integer
    
    """
    
    return {"message": f"blog id is {id}"}

# custom type
class BlogType(str, Enum):
    type1 = 'food'
    type2 = 'car'
    type3 = 'programming'


@router.get('/blog/type/{type}')
def blog_type(type: BlogType):
    return {'message': f'blog type is {type=}'}


def log_data(message):
    with open('log.txt', 'a') as file:
        file.write(message)

# custom status
@router.get('/blog', status_code = status.HTTP_200_OK)
def GetBlog(bt: BackgroundTasks, page:int, response:Response):
    bt.add_task(log_data, "get all blogs")
    if page > 20:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'page is {page=}'}
    
# default value
@router.get('/blog/')
def get_page(page:Optional[int]=1, number:int=None):
    return {'message': f'{page=} and {number=}'}