from ninja import Router
from typing import List
from .schemas import StudioSchema
from .models import Studio

router = Router(tags=['Studios'])

@router.get('/', response=List[StudioSchema])
def get_all(request):
  return Studio.objects.all()
