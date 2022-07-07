from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from typing import List, Optional


router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'clock', 'microphone']

@router.get('/')
def get_all():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.headers['my_header'] = 'test header!'
    response.set_cookie(key="cookie", value="test")
    return response


@router.get('/pro/{id}', responses={
    404: {"content": {"text/plain": {"example": "product not found"}}, "description":"product not found"},
    200: {"content": {"text/html": {"example": "<div> data </div>"}}, "description":"html code data "}
})
def get_product(id: int):
    if id > len(products):
        text = "product not found"
        return PlainTextResponse(content=text, media_type='text/plain', status_code=404)
        
    data = products[id]
    return HTMLResponse(content=f"<div> {data} </div>", media_type="text/html")


@router.get("/withheader")
def get_products(custom_header: Optional[List[str]] = Header(None), cookie: str = Cookie(None)):
        return {'data': products, "header": custom_header, "cookie": cookie}
    
    
@router.post('/create')
def create_product(data: str=Form(...)):
    products.append(data)
    return products