from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from backend.views import NumberViewSet, CreateRandomNumber, PokemonViewSet


router = DefaultRouter()
router.register(r'numbers', NumberViewSet)
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('random/', CreateRandomNumber.as_view(), name='create_random_number'),
    path('admin/', admin.site.urls),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

