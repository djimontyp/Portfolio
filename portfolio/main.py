from faker import Faker
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# from routers import parsers
from routers.parsers import parser

app = FastAPI(
    title='Portfolio',
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.include_router(parsers.parsers)


@app.get('/', response_class=HTMLResponse, name='index')
async def index(request_: Request):
    return templates.TemplateResponse('index/index.html', {
        'request': request_,
        'paragraphs': [Faker().paragraph(nb_sentences=40) for _ in range(7)],
        'long_right': Faker().paragraph(nb_sentences=400),
    })


@app.get('/parsers', response_class=HTMLResponse, name='parser')
def parser_index(request_: Request):
    return templates.TemplateResponse('parser/parser.html', {
        'request': request_,
    })


@app.get('/documentation', response_class=HTMLResponse, name='documentation')
def base(request_: Request):
    return templates.TemplateResponse('index/index.html', {
        'request': request_,
    })


@app.get('/content', response_class=HTMLResponse, name='content')
def content(request_: Request):
    return templates.TemplateResponse('content.html', {
        'request': request_,
        'products': parser(),
    })

