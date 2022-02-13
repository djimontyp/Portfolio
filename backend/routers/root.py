from faker import Faker
from starlette.requests import Request

from routers import templates


async def homepage(request: Request):
    """Root view - `About me`"""
    name = 'index.html'
    context = {
        'request': request,
        'paragraphs': [Faker().paragraph(nb_sentences=40) for _ in range(3)],
        'long_right': Faker().paragraph(nb_sentences=150),
    }
    return templates.TemplateResponse(name, context)


async def spotify(request: Request):
    """Spotify view"""
    name = 'spotify.html'
    context = {
        'request': request,
    }
    return templates.TemplateResponse(name, context)
