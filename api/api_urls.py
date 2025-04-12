from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MaquinaViewSet,
    PiezaViewSet,
    EncargadoViewSet,
    MantenimientoViewSet,
    TareaViewSet,
    PiezaMaquinaViewSet,
)

router = DefaultRouter()
router.register(r"maquinas", MaquinaViewSet)
router.register(r"piezas", PiezaViewSet)
router.register(r"encargados", EncargadoViewSet)
router.register(r"mantenimientos", MantenimientoViewSet)
router.register(r"tareas", TareaViewSet)
router.register(r"pieza-maquina", PiezaMaquinaViewSet)

urlpatterns = router.urls
