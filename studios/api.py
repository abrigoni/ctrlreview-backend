from typing import List

from ninja import Router

from .models import Studio
from .schemas import StudioSchema

router = Router(tags=["Studios"])


@router.get("/", response=List[StudioSchema])
def get_all(request):
    return Studio.objects.all()
