from typing import List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from config import get_settings
from schemas import Book, Item, UserTracks
from spotify import client

origins = ['*']

settings = get_settings()

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    contact={"email": settings.ADMIN_EMAIL}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', name='homepage')
async def homepage():
    return RedirectResponse('/docs')


@app.get('/books', response_model=List[Book], name='books')
async def books():
    return Book.all()


@app.get('/item', response_model=Item, name='parsers')
async def item() -> Item:
    return Item.get()


@app.get('/tracks', response_model=UserTracks, name='spotify_tracks')
def show_tracks():
    tracks = client.current_user_saved_tracks(limit=50)
    return UserTracks.parse_obj(tracks)

