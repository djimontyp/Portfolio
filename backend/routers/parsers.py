from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

from . import templates

router = APIRouter(prefix='/parsers')


@router.get('/', response_class=HTMLResponse, name='parsers')
async def get_parsers(request: Request):
    template_path = 'parser.html'
    context = {
        'request': request,
        'products': [
            {
                "src": "https://atlantmarket.com.ua/upload/iblock/7d4/13479.JPG.jpg",
                "title": "Ніж складний Ganzo G7361-WD1 дерево",
                "price": 1000,
                "article": "G7361-WD1"
            },
        ]
    }
    return templates.TemplateResponse(template_path, context)
