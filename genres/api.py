from typing import List

from ninja import Router

from .models import Genre
from .schemas import GenreSchema

router = Router(tags=["Genres"])


@router.get("/", response=List[GenreSchema])
def get_all(request):
    return Genre.objects.all()
