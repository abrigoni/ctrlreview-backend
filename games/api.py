from ninja import Router
from typing import List
from .schemas import GameSchema
from .models import Game


router = Router(tags=['Games'])

@router.get('/', response=List[GameSchema])
def get_all(request):
  return Game.objects.all()
