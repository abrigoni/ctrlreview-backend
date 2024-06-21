from ninja import Router
from typing import List
from .schemas import PlatformSchema
from .models import Platform

router = Router(tags=['Platforms'])

@router.get('/', response=List[PlatformSchema])
def get_all(request):
  return Platform.objects.all()
