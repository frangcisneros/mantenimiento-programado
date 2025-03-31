from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MaquinaViewSet,
    TareaMantenimientoViewSet,
    PiezaViewSet,
    TipoMantenimientoViewSet,
    EncargadoViewSet,
)

router = DefaultRouter()
router.register(r"maquinas", MaquinaViewSet)
router.register(r"tareas", TareaMantenimientoViewSet)
router.register(r"piezas", PiezaViewSet)
router.register(r"tipos_mantenimiento", TipoMantenimientoViewSet)
router.register(r"encargados", EncargadoViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
