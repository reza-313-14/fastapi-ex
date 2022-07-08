from fastapi import FastAPI, status
from router import blog_get, blog_post, user, article, product, file
from auth import authentication
from database import models
from database.db import engine
from exceptions import EmailNotValid
from fastapi.requests import Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocket
import time


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(file.router)
app.include_router(authentication.router)

app.mount('/files', StaticFiles(directory='files'), name='files')

models.Base.metadata.create_all(engine)

# first
@app.get('/', tags=['home'], summary="test summary!", description="hello world")
def home():
    return {"name": 'mahdi'}



@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.middleware('http')
async def add_middle_ware(request: Request, call_next):
    
    print(request.client)
    
    print("before")
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    print('after')
    return response