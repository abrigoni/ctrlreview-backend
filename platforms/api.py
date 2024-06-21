from ninja import NinjaAPI
from typing import List
from .schemas import PlatformSchema
from .models import Platform

api = NinjaAPI(urls_namespace='platforms')

@api.get('/', response=List[PlatformSchema])
def get_all(request):
  return Platform.objects.all()
