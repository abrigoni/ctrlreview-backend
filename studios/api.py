from ninja import NinjaAPI
from typing import List
from .schemas import StudioSchema
from .models import Studio

api = NinjaAPI(urls_namespace='studios')

@api.get('/', response=List[StudioSchema])
def get_all(request):
  return Studio.objects.all()
