from ninja import Schema
from typing import List
from datetime import date
from studios.schemas import StudioSchema
from genres.schemas import GenreSchema
from platforms.schemas import PlatformSchema

class GameSchema(Schema):
  id: int
  title: str
  description: str
  release_date: date
  image_url: str
  studio: StudioSchema
  platforms: List[PlatformSchema]
  genres: List[GenreSchema]
