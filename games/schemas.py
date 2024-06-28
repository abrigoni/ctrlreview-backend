from datetime import date
from typing import List

from ninja import Schema

from genres.schemas import GenreSchema
from platforms.schemas import PlatformSchema
from studios.schemas import StudioSchema


class GameSchema(Schema):
    id: int
    title: str
    description: str
    release_date: date
    image_url: str
    studio: StudioSchema
    platforms: List[PlatformSchema]
    genres: List[GenreSchema]
