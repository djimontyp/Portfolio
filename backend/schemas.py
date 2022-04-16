from datetime import datetime
from typing import List, Dict, Optional

from pydantic import BaseModel, conint, validator, HttpUrl

from utils import image_url


class Book(BaseModel):
    title: str
    image: str
    pages: conint(gt=0)  # pages > 0
    page: conint(ge=0)  # page >= 0

    @validator('image')
    def image_url_builder(cls, filename):
        return image_url(filename)

    @classmethod
    def all(cls) -> List["Book"]:
        return [
            cls(
                title="Чистый Python. Тонкости программирования для профи.",
                image="CleanPython.jpg",
                pages=288,
                page=288
            ),
            cls(
                title="Python. Разработка на основе тестирования.",
                image="TDD.jpg",
                pages=624,
                page=77,
            ),
        ]


class Item(BaseModel):
    title: str
    image: str
    price: conint(gt=0)  # price > 0
    article: str

    @classmethod
    def get(cls) -> "Item":
        return cls(
            image="https://atlantmarket.com.ua/upload/iblock/7d4/13479.JPG.jpg",
            title="Ніж складний Ganzo G7361-WD1 дерево",
            price=1000,
            article="G7361-WD1"
        )


class Track(BaseModel):
    album: Optional[Dict] = None
    artists: Optional[List] = None
    available_markets: List[str]
    disc_number: Optional[int] = None
    duration_ms: Optional[int] = None
    explicit: bool
    external_ids: Optional[Dict] = None
    external_urls: Optional[Dict] = None
    href: Optional[HttpUrl] = None
    id: Optional[str] = None
    is_local: bool
    name: Optional[str] = None
    popularity: Optional[int] = None
    preview_url: Optional[HttpUrl] = None
    track_number: Optional[int] = None
    type: Optional[str] = None
    uri: Optional[str] = None


class UserTrack(BaseModel):
    added_at: datetime
    track: Track


class UserTracks(BaseModel):
    href: Optional[HttpUrl] = None
    items: List[UserTrack] = []
    limit: Optional[int] = None
    next: Optional[HttpUrl] = None
    offset: Optional[int] = None
    previous: Optional[HttpUrl] = None
    total: Optional[int] = None
