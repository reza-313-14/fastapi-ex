from fastapi import FastAPI
from router import blog_get, blog_post, user
from database import models
from database.db import engine


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
models.Base.metadata.create_all(engine)

# first
@app.get('/', tags=['home'], summary="test summary!", description="hello world")
def home():
    return {"name": 'mahdi'}