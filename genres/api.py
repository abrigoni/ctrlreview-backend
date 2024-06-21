from ninja import NinjaAPI
from .models import Genre
from .schemas import GenreSchema
from typing import List

api = NinjaAPI()

@api.get('/', response=List[GenreSchema])
def get_all():
  return Genre.objects.all()

