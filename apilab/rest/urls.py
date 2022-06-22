from django.urls import include, path
from rest_framework import routers
from .views import EquipoViewSet

router = routers.DefaultRouter()
router.register(r'equipo', EquipoViewSet)

urlpatterns = [
    path('', include(router.urls))
]