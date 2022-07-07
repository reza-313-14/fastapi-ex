from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, PlainTextResponse


router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'clock', 'microphone']

@router.get('/')
def get_all():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get('/{id}', responses={
    404: {"content": {"text/plain": {"example": "product not found"}}, "description":"product not found"},
    200: {"content": {"text/html": {"example": "<div> data </div>"}}, "description":"html code data "}
})
def get_product(id: int):
    if id > len(products):
        text = "product not found"
        return PlainTextResponse(content=text, media_type='text/plain', status_code=404)
        
    data = products[id]
    return HTMLResponse(content=f"<div> {data} </div>", media_type="text/html")