from ninja import NinjaAPI
from typing import List
from .schemas import GenreSchema
from .models import Genre

api = NinjaAPI(urls_namespace='genres')

@api.get('/', response=List[GenreSchema])
def get_all(request):
  return Genre.objects.all()
