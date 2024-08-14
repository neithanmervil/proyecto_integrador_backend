from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispositivoViewSet, PrestamoViewSet

router = DefaultRouter()
router.register(r'dispositivos', DispositivoViewSet)
router.register(r'prestamos', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
