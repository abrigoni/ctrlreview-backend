from ninja import NinjaAPI
from typing import List
from .schemas import Schema
from .models import Game


api = NinjaAPI(urls_namespace='games')

@api.get('/', response=List[Schema])
def get_all(request):
  return Game.objects.all()
