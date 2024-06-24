from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from backend.views import *

from backend.views import NumberViewSet, CreateRandomNumber,PokemonViewSet

router = DefaultRouter()
router.register(r'numbers', NumberViewSet)
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('random/', CreateRandomNumber.as_view(), name='create_random_number'),
    path('admin/', admin.site.urls),
]
