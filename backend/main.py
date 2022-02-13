from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.routing import Route

from constants import STATIC_PATH_B
from routers.parsers import router as parsers_router
from routers.books import router as books_router
from routers.root import homepage, spotify

base_routes = [
    Route('/', homepage, name='homepage', methods=['GET']),
    Route('/spotify', spotify, name='spotify', methods=['GET']),
]

app = FastAPI(title='Portfolio', routes=base_routes)

app.mount(str(STATIC_PATH_B), StaticFiles(directory='static'), name="static")
app.include_router(parsers_router)
app.include_router(books_router)
