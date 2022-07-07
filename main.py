from fastapi import FastAPI, status
from router import blog_get, blog_post, user, article
from database import models
from database.db import engine
from exceptions import EmailNotValid
from fastapi.requests import Request
from fastapi.responses import JSONResponse


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
models.Base.metadata.create_all(engine)

# first
@app.get('/', tags=['home'], summary="test summary!", description="hello world")
def home():
    return {"name": 'mahdi'}


@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)