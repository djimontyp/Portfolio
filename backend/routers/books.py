from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

from constants import BOOKS_PATH_F
from . import templates

router = APIRouter(prefix='/books')


@router.get('/', response_class=HTMLResponse, name='books')
async def get_books_info(request: Request):
    template_path = 'books.html'
    context = {
        'request': request,
        'books': [
            {
                "title": "Чистый Python. Тонкости программирования для профи.",
                "image": request.url_for('static', path=str(BOOKS_PATH_F.joinpath("CleanPython.jpg"))),
                "total_pages": 288,
                "current_page": 288,
            },
            {
                "title": "Python. Разработка на основе тестирования.",
                "image": request.url_for('static', path=str(BOOKS_PATH_F.joinpath("TDD.jpg"))),
                "total_pages": 624,
                "current_page": 77,
            },
        ]
    }
    return templates.TemplateResponse(template_path, context)
