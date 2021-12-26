# from fastapi import APIRouter
# from fastapi.responses import HTMLResponse
# from starlette.requests import Request
# from starlette.templating import Jinja2Templates
#
# templates = Jinja2Templates(directory="templates")
#
#
# parsers = APIRouter(
#     prefix="/parsers",
# )
#
#
# @parsers.get('/', response_class=HTMLResponse, name='parser')
# def parser_index(request_: Request):
#     return templates.TemplateResponse(
#         'parser/parser.html',
#         {
#             'request': request_,
#         },
#     )


def parser():
    products_all = {
        "products": [
            {
                "src": "https://atlantmarket.com.ua/upload/iblock/7d4/13479.JPG.jpg",
                "title": "Ніж складний Ganzo G7361-WD1 дерево",
                "price": 1000,
                "article": "G7361-WD1"
            },
        ]
    }
    return products_all
