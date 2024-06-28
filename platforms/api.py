from typing import List

from ninja import Router

from .models import Platform
from .schemas import PlatformSchema

router = Router(tags=["Platforms"])


@router.get("/", response=List[PlatformSchema])
def get_all(request):
    return Platform.objects.all()
