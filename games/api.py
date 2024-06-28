from typing import List

from ninja import Router

from .models import Game
from .schemas import GameSchema

router = Router(tags=["Games"])


@router.get("/", response=List[GameSchema])
def get_all(request):
    return Game.objects.all()
