from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from genres.api import router as genres_router
from platforms.api import router as platforms_router
from studios.api import router as studios_router
from games.api import router as games_router
from users.api import router as users_router

api = NinjaAPI()

api.add_router(prefix='genres', router=genres_router)
api.add_router(prefix='platforms', router=platforms_router)
api.add_router(prefix='studios', router=studios_router)
api.add_router(prefix='games', router=games_router)
api.add_router(prefix='users', router=users_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
