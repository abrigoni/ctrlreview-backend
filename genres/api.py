from ninja import Router
from typing import List
from .schemas import GenreSchema
from .models import Genre

router = Router(tags=['Genres'])

@router.get('/', response=List[GenreSchema])
def get_all(request):
  return Genre.objects.all()
